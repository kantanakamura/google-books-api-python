# input fields for searching
search = {
    'free': '',
    'title': 'Python',
    'publisher': '',
    'subject': '',
    'isbn': '',
    'lccn': '',
    'oclc': '',
}

def url_q():
    title_q = '' if search['title']=='' else 'intitle:'+search['title']
    publisher_q = '' if search['publisher']== '' else 'inpublisher:'+search['publisher']
    subject_q = '' if search['subject']== '' else 'subject:'+search['subject']
    isbn_q = '' if search['isbn']== '' else 'isbn:'+search['isbn']
    lccn_q = '' if search['lccn']== '' else 'lccn:'+search['lccn']
    oclc_q = '' if search['oclc']== '' else 'oclc:'+search['oclc']
    q_list = [search['free'], title_q, publisher_q, subject_q, isbn_q, lccn_q, oclc_q]
    q_list_none = list(filter(None, q_list))
    url_q = 'q=' + '+'.join(q_list_none)
    return url_q



