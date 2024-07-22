#!/usr/bin/env python3
""" A Simple helper function """


def index_range(page, page_size):
    """ Function returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters. """
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index
