if __name__ == "__main__":
    import argparse
    from quizzer import Quizzer

    parser = argparse.ArgumentParser(description="Quizzer: A command-line quiz application.")
    parser.add_argument("quiz_file", help="Path to the quiz file (JSON format).")
    args = parser.parse_args()

    Quizzer(args.quiz_file)