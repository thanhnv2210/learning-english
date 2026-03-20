#!/usr/bin/env python3
"""
Simple collocations search CLI.
Usage:
  python3 search.py --word deploy
  python3 search.py --tag deploy
"""
import argparse
import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).with_name('data.json')


def load_data():
    if not DATA_FILE.exists():
        print(f"Data file not found: {DATA_FILE}")
        sys.exit(1)
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def search_by_word(data, word):
    word = word.lower()
    results = [e for e in data if e.get('headword','').lower() == word or word in e.get('collocation','').lower()]
    return results


def search_by_tag(data, tag):
    tag = tag.lower()
    results = [e for e in data if tag in [t.lower() for t in e.get('tags', [])]]
    return results


def pretty_print(entries):
    if not entries:
        print('No results')
        return
    for e in entries:
        print('---')
        print(f"Headword: {e.get('headword')}")
        print(f"Collocation: {e.get('collocation')}")
        print(f"Meaning: {e.get('meaning')}")
        print(f"Example: {e.get('example')}")
        print(f"Spoken cue: {e.get('spoken_cue')}")
        print(f"Tags: {', '.join(e.get('tags', []))}")


def main():
    parser = argparse.ArgumentParser(description='Search collocations')
    parser.add_argument('--word', help='search by headword or collocation')
    parser.add_argument('--tag', help='search by tag')
    args = parser.parse_args()

    data = load_data()
    results = []
    if args.word:
        results = search_by_word(data, args.word)
    elif args.tag:
        results = search_by_tag(data, args.tag)
    else:
        print('Please provide --word or --tag')
        parser.print_help()
        sys.exit(1)

    pretty_print(results)


if __name__ == '__main__':
    main()
