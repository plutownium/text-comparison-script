from os import chdir


file_path_blank = "H:\Ableton Projects/2016.07 July\TEST_blank Project"
file_path = "H:\Ableton Projects/2016.07 July\TEST_01 Project"


xml_blank = "test_blank.txt"
xml1 = "test_01.txt"


def open_xml(path, file):
    chdir(path)
    f = open(file, "rb")
    xml = str(f.read())
    f.close()
    return xml


empty_project = open_xml(file_path_blank, xml_blank)
proj_x = open_xml(file_path, xml1)


def compare(blank_text, text2, from_index=0, bump=0):
    """the 'bump' argument should result in """
    for i in range(from_index, len(blank_text)):
        if blank_text[i] == text2[i + bump]:
            pass
        elif i == len(blank_text):
            print("Done! There were {0} characters in the text.".format(i))
        else:
            failure_index = i
            buffer = make_buffer(blank_text, failure_index)
            restart_index = search_match(text2, failure_index, buffer)
            try:
                index_adjustment = int(restart_index) - int(failure_index)
                compare(blank_text, text2, from_index=restart_index,
                        bump=index_adjustment)
            except TypeError:
                print("Done!")
                break


def make_buffer(text, index, length=5):
    end_buffer = index + length
    the_buffer = text[index:end_buffer]
    return the_buffer


def search_match(text_to_search, from_index, buffer_text):
    """text_to_search == the file with differing contents.
    from_index == the index where characters started to be different.
    buffer_text == the string we are comparing against."""
    buffer_size = len(buffer_text)
    for index in range(from_index, len(text_to_search)):
        end_index = index + buffer_size
        test_material = text_to_search[index:end_index]
        if test_material == buffer_text:
            # Return the index because at this point, the chars appears to be
            # the same in both texts.
            restart_index = index
            return restart_index
        else:
            # print("Comparing {0} to {1}.".format(test_material, buffer_text))
            pass

# compare(empty_project, proj_x)
