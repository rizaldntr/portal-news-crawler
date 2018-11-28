CONFIG = {
    'KOMPAS': {
        'NAME': 'Kompas',
        'START': 'https://indeks.kompas.com/news/%s',
        'ARTICLES': '//a[@class="article__link"]/@href',
        'NEXT_PAGES': '//div[@class="paging__wrap clearfix"]//a/@href',
        'TITLE': '//h1[@class="read__title"]/text()',
        'AUTHOR': '//div[@class="read__author"]/a/text()',
        'DATE': '//div[@class="read__time"]/text()',
        'TAG': '//ul[@class="tag__article__wrap"]//text()',
        'CATEGORY': '//ul[@class="breadcrumb__wrap"]/li[3]/a//text()',
        'CONTENTS': '//div[@class="read__content"]//text()',
        'EXCLUDE_TEXT': r'Baca Juga:',
    },
    'DETIK': {
        'NAME': 'Detik',
        'START': 'https://news.detik.com/indeks/all?date=%s',
        'ARTICLES': '//article//a/@href',
        'NEXT_PAGES': '//div[@class="paging paging2"]//a/@href',
        'TITLE': '//div[@class="jdl"]//h1/text()',
        'AUTHOR': '//div[@class="jdl"]//div[@class="author"]//text()',
        'DATE': '//div[@class="jdl"]//div[@class="date"]//text()',
        'TAG': '//div[@class="detail_tag"]/a/text()',
        'CATEGORY': '//div[@class="breadcrumb"]/a[2]/text()',
        'CONTENTS': '//div[@id="detikdetailtext"]//text()',
        'EXCLUDE_LINK': '// table[@class = "linksisip"]//text()',
        'EXCLUDE_TEXT': r'Tonton juga|Tonton video|detik]',
        'STOP_CRITERION': r'\(\S+\/\S+\)'
    },
    'TRIBUN': {
        'NAME': 'Tribun',
        'START': 'http://www.tribunnews.com/index-news?date=%s',
        'ARTICLES': '//h3[@class="f16 fbo"]/a/@href',
        'NEXT_PAGES': '//div[@id="paginga"]//a/@href',
        'TITLE': '//h1[@id="arttitle"]/text()',
        'AUTHOR': '//div[@id="editor"]/text()',
        'DATE': '//time/text()',
        'TAG': '//h5[@class="tagcloud3"]//text()',
        'CATEGORY': '//li[@itemprop="itemListElement"][2]/h4/a/span/text()',
        'CONTENTS': '//div[@class="side-article txt-article"]//text()',
        'EXCLUDE_LINK': '//div[@class="side-article txt-article"]/script/text() | //p[@class="baca"]//text()',
    },
    'TEMPO': {
        'NAME': 'Tempo',
        'START': 'https://www.tempo.co/indeks/%s',
        'ARTICLES': '//div[@class="card card-type-1"]//a[1]/@href',
        'NEXT_PAGES': '/',
        'TITLE': '//article/h1//text()',
        'AUTHOR': '//div[@id="author"][2]/h4/text()',
        'DATE': '//span[@id="date"]/text()',
        'TAG': '//div[@class="tags clearfix"]/li/a/text()',
        'CATEGORY': '//nav[@class="breadcrumbs"]/li[3]/a/span/text()',
        'CONTENTS': '//div[@id="isi"]//text()',
        'EXCLUDE_LINK': '//div[@id="isi"]/p/strong/a/text()',
        'EXCLUDE_TEXT': r'Baca:',
    },
    'CNN': {
        'NAME': 'CNN',
        'START': 'https://www.cnnindonesia.com/indeks?date=%s&p=%s&date=%s&kanal=2',
        'ARTICLES': '//article/a/@href',
        'NEXT_PAGES': '/',
        'TITLE': '//h1[@class="title"]/text()',
        'AUTHOR': '/',
        'DATE': '//div[@class="date"]/text()',
        'TAG': '//div[@class="detail_tag mb20"]/a/text()',
        'CATEGORY': '//a[@class="gtm_breadcrumb_kanal"]//text()',
        'CONTENTS': '//span[@id="detikdetailtext"]//text()',
    },
    'REPUBLIKA': {
        'NAME': 'Republika',
        'START': 'https://www.republika.co.id/index/%s',
        'ARTICLES': '//div[@class="txt_subkanal txt_index"]/h2/a/@href',
        'NEXT_PAGES': '//nav[@role="navigation"]/a/@href',
        'TITLE': '//div[@class="wrap_detail_set"]/h1/text()',
        'AUTHOR': '//div[@class="by"]/span/p/text()',
        'DATE': '//div[@class="date_detail"]/p/text()',
        'TAG': '//div[@class="wrap_blok_tag"]/ul/li/h1/a/text()',
        'CATEGORY': '//div[@class="breadcome"]/ul/li[2]/a/text()',
        'CONTENTS': '//div[@class="artikel"]//text()',
    },
    'USER_AGENT': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0",
    'ALLOWED_DOMAIN': [
        'www.tribunnews.com',
        'news.detik.com',
        'kompas.com',
        'tempo.co',
        'www.cnnindonesia.com',
        'republika.co.id'
    ]
}


# CONFIG = {
#     'DETIK': {
#         'NAME': 'None',
#         'START': 'Lorem Ipsum',
#         'ARTICLES': 'Lorem Ipsum',
#         'NEXT_PAGES': 'Lorem Ipsum',
#         'TITLE': 'Lorem Ipsum',
#         'AUTHOR': 'Lorem Ipsum',
#         'DATE': 'Lorem Ipsum',
#         'TAG': 'Lorem Ipsum',
#         'CATEGORY': 'Lorem Ipsum',
#         'CONTENTS': 'Lorem Ipsum',
#         'EXCLUDE_LINK': 'Lorem Ipsum',
#         'EXCLUDE_TEXT': r'Lorem Ipsum',
#         'STOP_CRITERION': r'Lorem Ipsum'
#     },
# }
