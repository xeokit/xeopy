class TextTools:

    @staticmethod
    def merge_taken_tuples_to_set(list_of_objects_to_get_tuples_from, tuple_method_name):

        result = set()
        for object_to_get_tuples_from in list_of_objects_to_get_tuples_from:
            if isinstance(object_to_get_tuples_from, list):
                for flattened_object_to_get_tuples_from in object_to_get_tuples_from:
                    taken_tuple = getattr(flattened_object_to_get_tuples_from, tuple_method_name)
                    for tuple_element in taken_tuple():
                        result.add(tuple_element)
            else:
                taken_tuple = getattr(object_to_get_tuples_from, tuple_method_name)
                for tuple_element in taken_tuple():
                    result.add(tuple_element)
        return result

