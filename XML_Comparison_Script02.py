from os import chdir
import itertools


file_path_blank = "H:\Ableton Projects/2016.07 July\TEST_blank Project"
file_path = "H:\Ableton Projects/2016.07 July\TEST_01 Project"
# file_path2 = "H:\Ableton Projects/2016.07 July\TEST_02 Project"

xml_blank = "test_blank.txt"
xml1 = "test_01.txt"
# xml2 = "test_02.txt"


def open_xml(path, file):
    chdir(path)
    f = open(file, "rb")
    xml = str(f.read())
    f.close()
    return xml


empty_project = open_xml(file_path_blank, xml_blank)
proj_x = open_xml(file_path, xml1)
# proj_y = open_xml(file_path2, xml2)


# Compare blank file to the file with one sample in an audio channel.
# It is a 200,000+ letter text file.
# 0) Compare letter by letter. If there is no difference, do nothing.
# But when there is a difference...
# a) report the index where the difference in characters began.
# b) Load a "buffer" of 5 characters, starting from the blank project
#    file's text, starting from the index where the difference began.
#    (Report also what buffer was chosen.)
# c) Using the buffer to compare, interrupt the process of
#    letter by letter comparison, and compare the non-empty proj to the
#    buffer. Progress from the index where the || ("difference") was spotted
#    until a match for the buffer is found in the non-empty proj.
# d) When the non-empty project seems to match the blank project again,
#    pick up comparing letter by letter again.


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

test_text_one_a = """This is a sentence. Here are some words. I like to type.
                Testing code is fun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is fun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is fun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is fun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is fun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is fun. Who likes to code? I sure do."""
test_text_one_b = """This is a sentence. Here are some words. I like to type.
                Testing code is f234@$$sun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is f234@$$sun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is f234@$$sun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is f234@$$sun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is f234@$$sun. Who likes to code? I sure do.This is a sentence. Here are some words. I like to type.
                Testing code is f234@$$sun. Who likes to code? I sure do."""

compare(test_text_one_a, test_text_one_b)
