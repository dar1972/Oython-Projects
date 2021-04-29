"""
File: dna.py
Language: Python3
Author: Dhruv Rajpurohit
Description:
"""

import linked_code


def convert_to_nodes(dna_string):
    """
    This function is used to make a linked list
    :param dna_string: DNA string which is being converted to linked list
    :return:the linked list
    """
    str = ""
    if dna_string != str:
        return linked_code.LinkNode(dna_string[0], convert_to_nodes(dna_string[1:]))
    else:
        return None


def convert_to_string(dna_seq):
    """
    Linked node is converted to string
    :param dna_seq: the sequence which is being converted
    :return:the string of the sequence
    """
    string = ""
    while dna_seq is not None:
        string += dna_seq.value
        dna_seq = dna_seq.rest
    return string


def is_match(dna_seq1, dna_seq2):
    """
    to compare two different nodes if they are the same
    :param dna_seq1:first sequence which is being converted
    :param dna_seq2:second sequence which is being converted
    :return:the matched result
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    if dna_seq1 is None or dna_seq2 is None:
        return False
    if dna_seq1.value != dna_seq2.value:
        return False
    if dna_seq1.value == dna_seq2.value:
        return is_match(dna_seq1.rest, dna_seq2.rest)


def is_pairing(dna_seq1, dna_seq2):
    """
    to check if two pair are the same
    :param dna_seq1: first sequence
    :param dna_seq2: second sequence
    :return: the matched result
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    if dna_seq1 is None or dna_seq2 is None:
        return False
    if dna_seq1.value == 'A' and dna_seq2.value != 'T':
        return False
    if dna_seq1.value == 'A' and dna_seq2.value == 'T':
        return is_pairing(dna_seq1.rest, dna_seq2.rest)
    if dna_seq1.value == 'T' and dna_seq2.value != 'A':
        return False
    if dna_seq1.value == 'T' and dna_seq2.value == 'A':
        return is_pairing( dna_seq1.rest, dna_seq2.rest )
    if dna_seq1.value == 'G' and dna_seq2.value != 'C':
        return False
    if dna_seq1.value == 'G' and dna_seq2.value == 'C':
        return is_pairing( dna_seq1.rest, dna_seq2.rest )
    if dna_seq1.value == 'C' and dna_seq2.value != 'G':
        return False
    if dna_seq1.value == 'C' and dna_seq2.value == 'G':
        return is_pairing( dna_seq1.rest, dna_seq2.rest )


def is_palindrome(dna_seq):
    """
    checks if the node is a palindrome
    :param dna_seq: the sequence
    :return: result of the palindrome
    """
    if (linked_code.length_iter(dna_seq)) % 2 != 0:
        med = ((linked_code.length_iter(dna_seq))//2)
    else :
        med = ((linked_code.length_iter(dna_seq))/2)-1
    i = 0
    j = (linked_code.length_iter(dna_seq))-1
    if(dna_seq!=None):
        while j>i:
            if (linked_code.value_at(dna_seq,i)) == (linked_code.value_at(dna_seq,j)):
                i += 1
                j -= 1
            else:
                return False
        return True
    elif(dna_seq==None):
        return True
    else:
        return False


def substitution(dna_seq1, idx, base):
    """
    base is substituted with another base
    :param dna_seq1: DNA sequence
    :param idx: index value
    :param base: base
    :return:
    """
    if linked_code.length_iter(dna_seq1)-1 >= idx:
        dna_seq1 = linked_code.insert_at( idx, base, dna_seq1)
        dna_seq1 = linked_code.remove_at( idx+1, dna_seq1 )
        return dna_seq1
    else:
        raise IndexError("Index out of Range")


def insertion(dna_seq1, dna_seq2, idx):
    """
    link one insterted to link two
    :param dna_seq1: first sequence
    :param dna_seq2: second sequence
    :param idx: index value
    :return: the inserted list
    """
    if idx == 0:
        return linked_code.concatenate(dna_seq2, dna_seq1)
    elif dna_seq1 is None:
        raise IndexError("Index out of Range")
    return linked_code.LinkNode(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, idx-1))


def deletion(dna_seq, idx, segment_size):
    """
    delete a segment from the sequence at the index value
    :param dna_seq: sequence from which deletion occurs
    :param idx: index value
    :param segment_size: segment to be deleted
    :return: new list
    """
    if segment_size > 0:
        dna_seq = linked_code.remove_at(idx, dna_seq)
        return deletion(dna_seq, idx, segment_size-1)
    if segment_size == 0:
        return dna_seq


def duplication(dna_seq, idx, segment_size):
    """
    a segment is duplicated and placed after the segment itsel
    :param dna_seq: the dna sequence
    :param idx: index value
    :param segment_size: the size of segment
    :return: the new list
    """
    if segment_size != 0:
        size = segment_size
        for i in range(segment_size):
            val = linked_code.value_at(dna_seq, idx)
            dna_seq = linked_code.insert_at(idx+size, val, dna_seq)
            idx += 1
            segment_size -= 1
        return dna_seq
    else:
        return dna_seq



