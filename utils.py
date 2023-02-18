from IPython.display import display_html
from itertools import chain,cycle

def display_side_by_side(*args,titles=cycle([''])):
    """
    Displays pandas dataframes side by side.
    titles is an optional list of titles to display with the dataframe
    https://stackoverflow.com/a/44923103
    """

    html_str=''

    for dataframe, title in zip(args, chain(titles,cycle(['</br>'])) ):
        html_str+='<th style="text-align:center"><td style="vertical-align:top">'
        html_str+=f'<h2 style="text-align: center;">{title}</h2>'
        html_str+=dataframe.to_html().replace('table','table style="display:inline"')
        html_str+='</td></th>'
    
    display_html(html_str,raw=True)
  