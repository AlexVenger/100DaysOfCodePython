def blog_to_dict(blog):
    blog_dict = blog.__dict__
    blog_dict.pop("_sa_instance_state")
    return blog


def blogs_to_list(blogs):
    blog_list = []
    for blog in blogs:
        blog_dict = blog_to_dict(blog)
        blog_list.append(blog_dict)
    return blog_list
