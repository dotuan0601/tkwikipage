# Overview

Using TkWikiPage tool to generate MD file and publish to wiki page

##### Requirement package: #####
* Pandas (pandas==0.23.4)
* Python gitlab (python-gitlab==1.8.0)
* TkWikiPage (tkwikipage==1.3)
##### Create new section: #####
``` 
    new_section = Section('section name here')
 ```

# Block

One Paragraph of project description goes here

Sample code

``` 
    section1 = Section('Block')
    section1.block('Give examples')
 ```

``` Give examples ```

# Hyperlink and ul, li

Sample code

``` 
section2.hyperlink('google', 'http://google.com')

for i in range(0, 4):
    section2.li(i)
 ```

[google](http://google.com)
* 0
* 1
* 2
* 3
# Combine hyperlink and normal text

##### 
TkWikipage has also provider a helper class named HelperDocs which includes functions:
- hyper(text, link)
- text(text, style='bold')
- text_combine(text, styles=[])
Currently, we supprot three styles: bold, italic and strike-throught
 #####
Sample code

``` 
section3.li('{} - The web framework used'.format(HelperDocs.hyper('dropwizard', 'https://google.com')))
section3.li('{} - Dependency Management'.format(HelperDocs.hyper('Maven', 'https://google.com')))
section3.li('{} - Used to generate RSS Feeds'.format(HelperDocs.hyper('ROME', 'https://google.com')))
 ```

* [dropwizard](https://google.com) - The web framework used
* [Maven](https://google.com) - Dependency Management
* [ROME](https://google.com) - Used to generate RSS Feeds
# Images

Sample code

``` 
section5.image('https://d33wubrfki0l68.cloudfront.net/eab45e25bb79970178fab7a2d10cba0209372a59/94d9e/assets/images/philly-magic-garden.jpg', 'fact design')
 ```

And you can see the result

![fact design](https://d33wubrfki0l68.cloudfront.net/eab45e25bb79970178fab7a2d10cba0209372a59/94d9e/assets/images/philly-magic-garden.jpg)

# Text styling

##### using HelperDocs class and multi_content_part function #####
Sample code

``` 
bold_text_in_section = HelperDocs.text('bold text', 'bold')
italic_text_in_section = HelperDocs.text('bold text', 'italic')
strike_text_in_section = HelperDocs.text('strike-throught text', 'strike-throught')
section6.multi_content_part([bold_text_in_section, italic_text_in_section, strike_text_in_section])
 ```

**bold text**

*bold text*

~~strike-throught text~~

# Table from two dimentional list

# You can display a two dimentional list simply with table function #
``` 
section7.table([('ten', 'tuoi'), ('tuan', 30)])
 ```

|ten|tuoi|
|-|-|
|tuan|30|
# Table from pandas dataframe

##### TkWikiPage also provide function to display pandas dataframe as table #####
``` 
pd_mapping = pd.read_csv('mapping.csv')
section8.df_to_table(pd_mapping.head())
 ```

|provider|resource|column|mapping|type|domain|comment|
|-|-|-|-|-|-|-|
|asia|dmvt|ma_vt|sku_id|default|product_info|nan|
|asia|dmvt|ten_vt|sku_name|default|product_info|nan|
|asia|dmvt|ma_nhom|cat_id|default|product_info|nan|
|asia|dmnhvt|ten_nhom|cat_name|default|product_info|nan|
|asia|dmnhvt|ma_nganh|cat_group_id|default|product_info|nan|
# Checkbox as task list

``` 
section9.description('Report status:')
section9.checked_list([
    'EOD', 'Region', 'CAT', 'Showroom'
], [0, 1, 2])
 ```

Report status:

- [x] EOD
- [x] Region
- [x] CAT
- [ ] Showroom
# Make MD file or publish all sections to gitlab


After you define sections content, you can export sections content to file .md or publish to gitlab which present step by step bellow


##### Init GitlabWikiPage #####
``` 
page = GitlabWikiPage(
    'gitlab link', //https://git.teko.vn
    'gitlab token', //P3PW4zufio5G1Pexxxxx
    'gitlab project', //data/docs
    'gitlab wiki page name'
)
 ```

##### Afterthat, add sections content to page and call render function or toMd function #####
``` 
page.add_section(overview)
page.add_section(section1)
.........................
 ```

``` 
page.toMd('test')
or 
page.publish()
 ```

