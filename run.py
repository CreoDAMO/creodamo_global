from creodamo import CreoDAMO
import argparse

def main():
    parser = argparse.ArgumentParser(description='Run CreoDAMO Platform')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    args = parser.parse_args()

    damo = CreoDAMO(debug=args.debug)
    damo.start()

if __name__ == '__main__':
    main()
