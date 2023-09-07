def cafe_to_dict(cafe):
	cafe_dict = cafe.__dict__
	cafe_dict.pop("_sa_instance_state")
	return cafe_dict


def cafes_to_list(cafes):
	cafe_list = []
	for cafe in cafes:
		cafe_dict = cafe_to_dict(cafe)
		cafe_list.append(cafe_dict)
	return cafe_list
