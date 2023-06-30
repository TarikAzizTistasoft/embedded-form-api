from django import template

register = template.Library()

def filter_by_parentcategory(subcategories, parentcategory_id):
    """
    Filters subcategories based on the provided parent category ID.

    Args:
        subcategories (QuerySet): The queryset of subcategories to filter.
        parentcategory_id (Any): The ID of the parent category to filter by.

    Returns:
        QuerySet: The filtered subcategories queryset.
    """

    if isinstance(subcategories, list):
        subcategories = filter(lambda x: x['parentcategory'] == parentcategory_id, subcategories)
    else:
        subcategories = subcategories.filter(parentcategory=parentcategory_id)
    
    return subcategories

def subcategory_issue_count(data, subcategories):
    """
    Custom filter to calculate the count of issues for specified subcategories.
    """
    count = 0
    for subcategory in subcategories:
        key = subcategory['data_key']
        count += data[key]
    # print(count)
    return count

def dict_lookup(dictionary, key):
    """
    Looks up a value in a dictionary using a dynamic key.

    Args:
        dictionary (dict): The dictionary to perform the lookup on.
        key (Any): The key to use for the lookup.

    Returns:
        Any: The value associated with the key in the dictionary, or None if the key is not found.
    """
    return dictionary.get(key, None)


register.filter("filter_by_parentcategory", filter_by_parentcategory)

register.filter("subcategory_issue_count", subcategory_issue_count)

register.filter("dict_lookup", dict_lookup)
