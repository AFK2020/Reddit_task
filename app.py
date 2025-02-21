import argparse
import csv
import os

import fpdf
import praw
from dotenv import load_dotenv

from constants import SubredditType

load_dotenv()


def run_pipeline(subreddit_names, limit, score_value, type_name):
    file_to_write = []
    for i in range(len(subreddit_names)):
        # for each value of subreddit name and it's corresponding type
        list = fetch_subreddit(subreddit_names[i],
                               limit, score_value, type_name[i])
        file_to_write.append(list)

    file_data = write_to_csv(file_to_write)
    write_to_pdf(file_data)


def fetch_subreddit(subreddit_name, limit, score_value, type_name):
    zipped_list = []
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent=os.getenv("USER_AGENT")
    )
    subred = reddit.subreddit(subreddit_name)
    post = get_posts_for_type(subred, str(type_name), limit)
    generator_results = filter(lambda post: (post.score > score_value), post)
    for p in generator_results:
        title = [p.title]
        url = [p.url]
        score = [p.score]
        name = [subreddit_name]
        type = [type_name]
        result = list(zip(name, type, title, url, score))
        zipped_list.extend(result)
    return zipped_list


def get_posts_for_type(subred_info, type_name, limit):
    if type_name == SubredditType.HOT.value:
        type_subreddit = subred_info.hot(limit=limit)
    elif type_name == SubredditType.CONTROVERSIAL.value:
        type_subreddit = subred_info.controversial(limit=limit)
    elif type_name == SubredditType.TOP.value:
        type_subreddit = subred_info.top(limit=limit)
    elif type_name == SubredditType.NEW.value:
        type_subreddit = subred_info.new(limit=limit)
    elif type_name == SubredditType.BEST.value:
        type_subreddit = subred_info.best(limit=limit)
    return type_subreddit


def write_to_csv(list):
    file_path = "file.csv"
    header_list = [["Subreddit", "Type", "Title", "URL", "Score"]]
    for i in range(len(list)):
        header_list.append(list[i])
    with open(file_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(header_list)  # Write all rows
    return header_list


def write_to_pdf(list):
    file_name = "file.pdf"
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for text in list:
        pdf.write(5, str(text))     # 5 is line height, i is string to print
        pdf.ln()    # line break, height of break can be given as argument
    pdf.output(file_name)


def list_of_strings(arg):
    return arg.split(',')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Parse multiple inputs")
    parser.add_argument("subreddit_name", type=list_of_strings,
                        help="Name of subreddit")
    parser.add_argument("--post_limit", type=int, default=10,
                        help="post limit")
    parser.add_argument("--post_score", type=int, default=15,
                        help="minimum post score")
    parser.add_argument("post_type", type=list_of_strings,
                        help="specify: hot, controversial, top")
    args = parser.parse_args()
    post_subreddit = args.subreddit_name
    post_limit = args.post_limit
    post_score = args.post_score
    post_type = args.post_type
    if post_limit > 0 and post_limit < 10000:
        run_pipeline(post_subreddit, post_limit, post_score, post_type)
