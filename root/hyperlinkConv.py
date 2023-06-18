

# у нас есть два типа метода который обрабатывает Гипперссылку


def handle_text(text):
    links=[
    '<a href="/construction_helicop/helicopter_cabin/">&1</a>',
    '<a href="/">&2</a>',
    '<a href="/construction_helicop/page1/">&3</a>'
    ]
    data_h=[]
    data_w=[]

    text2=text.split(' ')
    for word in text2:
        if word[0]=='&':
            link_number=word[0]+word[1]
            for link in links:
                if link_number in link:
                    l=link.split(link_number)
                    hyperlink=l[0]+word[2:]+l[1]
                    data_h.append(hyperlink)
                    data_w.append(word)
    new_text=text
    for i in range(len(data_h)):
        new_text=new_text.replace(data_w[i], data_h[i])
    print(new_text)    
    return new_text
def handle_text_urlJson(text, url):
    links=['<a href="/#/">', '</a>']
    save_word=l2=''
    text2=text.split(' ')
    
    for word in text2:
        if word[0]=='&':
            save_word=word
            new_l=links[0].replace('#', url)
            l2=new_l+word[2:]+links[1]
    new_text=text
    new_text=new_text.replace(save_word, l2)
    print(new_text)    
    return new_text