import lxml.etree

# Parse the HTML file using lxml.etree
tree = lxml.etree.parse('Welcome to Python.html', lxml.etree.HTMLParser())

# Specify the correct XPath expression to find the <ul> element
ul_elements = tree.xpath('//*[@id="content"]/div/section/div[3]/div[1]/div/ul')

ul_element = ul_elements[0]  # Assuming there is only one <ul> element
ul_text_content = lxml.etree.tostring(ul_element, method='text', encoding='utf-8').decode('utf-8')
print(ul_text_content)


