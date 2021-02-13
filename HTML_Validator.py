#!/bin/python3

import re


def validate_html(html):
    '''
    This function performs a limited version of html validation
    by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate
    # a list of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and
    # the code from class will be that you will have
    # to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags

    tags = _extract_tags(html)
    stack = []
    for symbol in tags:
        # check for opening tags
        if '/' not in symbol:
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return False
            if stack[-1][1:] == symbol[2:]:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant
    to be used directly
    by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained
    in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    tags = []
    # verify input has tag(s)
    if '<' in html or '>' in html:
        for i, symbol in enumerate(html):
            if symbol == '<':
                start = i
            if symbol == '>':
                end = i+1
                tags.append(html[start:end])
        if len(tags) == 0:
            tags.append(html[start:])
    clean_tags = []
    for t in tags:
        if re.search('^<.* .*>$', t):
            tag_no_attr = re.sub(' .*>$', re.search(' .*>', t).group()[-1], t)
            clean_tags.append(tag_no_attr)
        else:
            clean_tags.append(t)
    return clean_tags
