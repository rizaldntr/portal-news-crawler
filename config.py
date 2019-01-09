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
    'SINDO': {
        'NAME': 'Sindo',
        'START': 'https://index.sindonews.com/index/0?t=%s',
        'ARTICLES': '//div[@class="indeks-title"]/a/@href',
        'NEXT_PAGES': '//div[@class="pagination"]/ul/li/a/@href',
        'TITLE': '//div[@class="article"]/h1/text()',
        'AUTHOR': '//a[@rel="author"]/text()',
        'DATE': '//time/text()',
        'TAG': '//div[@class="tag-list"]/ul/li/a/text()',
        'CATEGORY': '//ul[@class="breadcrumb"]/li[2]//text()',
        'CONTENTS': '//div[@id="content"]//text()',
    },
    'LIPUTAN6': {
        'NAME': 'Liputan6',
        'START': 'https://www.liputan6.com/news/indeks/%s',
        'ARTICLES': '//h4[@class="articles--rows--item__title"]/a/@href',
        'NEXT_PAGES': '//ul[@class="simple-pagination__page-numbers js-pagination"]/li/a/@href',
        'TITLE': '//h1[@class="read-page--header--title entry-title"]//text()',
        'AUTHOR': '//span[@class="read-page--header--author__name fn"]/text()',
        'DATE': '//time[@class="read-page--header--author__datetime updated"]/text()',
        'TAG': '//ul[@class="tags--snippet__list"]/li/a/span/text()',
        'CATEGORY': '//li[@class="read-page--breadcrumb--item"][2]//text()',
        'CONTENTS': '//div[@class="article-content-body article-content-body_with-aside"]//text()',
        'EXCLUDE_LINK': '//div[@class="baca-juga"]//text()',
        'EXCLUDE_TEXT': r'Baca Juga|Saksikan video pilihan di bawah ini:',
        'STOP_CRITERION': r'Sumber: .*',
    },
    'BERITASATU': {
        'NAME': 'Berita Satu',
        'START': 'http://www.beritasatu.com/newsindex?indate=%s',
        'ARTICLES': '//div[@class="media custom-media-index"]/div[@class="media-body"]/a/@href',
        'NEXT_PAGES': '//ul[@class="pagination modal-1"]/li/a/@href',
        'TITLE': '//div[@class="title_post landing-headline frr"]/h1/text()',
        'AUTHOR': '//span[@class="hz_post_by"]/text()',
        'DATE': '//span[@class="hz_date_post"]/text()',
        'TAG': '/',
        'CATEGORY': '/',
        'CONTENTS': '//div[@class="hz_content mr"]//text()',
        'STOP_CRITERION': r'Sumber: '
    },
    'BISNIS': {
        'NAME': 'Bisnis',
        'START': 'https://www.bisnis.com/index?c=0&d=%s',
        'ARTICLES': '//ul[@class="l-style-none"]/li/div[2]/a/@href',
        'NEXT_PAGES': '//ul[@class="pagination"]/li/a/@href',
        'TITLE': '//div[@class="col-custom left"]/h1/text()',
        'AUTHOR': '//div[@class="author"]/text()',
        'DATE': '//div[@class="author"]/text()',
        'TAG': '//div[@class="tags"]/a/text()',
        'CATEGORY': '//ol[@class="breadcrumb"]/li[2]/a/span/text()',
        'CONTENTS': '//div[@class="description"]/div[@class="row"]/div[@class="col-sm-10"]//text()'
    },
    'MEDIAINDONESIA': {
        'NAME': 'Media Indonesia',
        'START': 'http://mediaindonesia.com/read',
        'ARTICLES': '//div[@class="article-content"]/h2/a/@href',
        'NEXT_PAGES': '//div[@class="pagination"]/a/@href',
        'TITLE': '//div[@class="article-title"]/h1/b/text()',
        'AUTHOR': '//div[@class="author"]/div[@class="a-content"]/span/b/text()',
        'DATE': '//div[@class="article-title"]/div/div/span[@class="meta"]/text()',
        'TAG': '//div[@class="article-tags tag-cloud"]/a/text()',
        'CATEGORY': '/',
        'CONTENTS': '//div[@itemprop="articleBody"]//text()',
        'EXCLUDE_LINK': '//div[@itemprop="articleBody"]//a/text() | //div[@class="dable_placeholder"]//text()',
        'EXCLUDE_TEXT': r'Baca juga:',
        'ART_DATE': '//div[@class="article-content"]/span/a[2]/text()'
    },
    'ANTARANEWS': {
        'NAME': 'Antara News',
        'START': 'https://www.antaranews.com/terkini',
        'ARTICLES': '//article[@class="simple-post simple-big clearfix"]/header/h3/a/@href',
        'NEXT_PAGES': '//ul[@class="pagination pagination-sm"]/li/a/@href',
        'TITLE': '//h1[@class="post-title"]/text()',
        'AUTHOR': '//p[@class="text-muted small"]//text()[2]',
        'DATE': '//span[@class="article-date"]/text()',
        'TAG': '//ul[@class="tags-widget clearfix"]/li/a/text()',
        'CATEGORY': '/',
        'CONTENTS': '//div[@class="post-content clearfix"]//text()',
        'EXCLUDE_LINK': '//b//text()',
        'STOP_CRITERION': r'Baca juga: ',
        'ART_DATE': '//article[@class="simple-post simple-big clearfix"]/header/p/span/text()'
    },
    'OKEZONE': {
        'NAME': 'Okezone',
        'START': 'https://index.okezone.com/bydate/index/%s',
        'ARTICLES': '//h4[@class="f17"]/a/@href',
        'NEXT_PAGES': '//div[@class="pagination-indexs"]//a/@href',
        'TITLE': '//div[@class="title"]/h1/text()',
        'AUTHOR': '//div[@class="namerep"]/text()',
        'DATE': '//div[@class="namerep"]/b/text()',
        'TAG': '//div[@class="detail-tag"]/ul/li/a/text()',
        'CATEGORY': '//div[@class="breadcrumb"]/ul/li[2]/a/text()',
        'CONTENTS': '//div[@id="contentx"]//p//text()',
        'EXCLUDE_TEXT': r'.*baca juga.*',
    },
    'VIVA': {
        'NAME': 'VIVA',
        'START': 'https://www.viva.co.id/request/indeks',
        'ARTICLES': '//a[@class="title-content"]/@href',
        'NEXT_PAGES': '/',
        'TITLE': '//div[@class="leading-title"]/h1/text()',
        'AUTHOR': '//meta[@property="dable:author"]/@content',
        'DATE': '//div[@class="date"]/text()',
        'TAG': '//meta[@name="keywords"]/@content',
        'CATEGORY': '//li[@itemprop="itemListElement"][1]//text()',
        'CONTENTS': '//div[@id="article-detail-content"]//text()',
        'EXCLUDE_LINK': '//div[@class="article-list lihat-juga lihat-juga-2"]//text()',
        'FORM_DATA': {
            'channel_name': 'all',
            'subchannel_name': 'all',
            'type': 'art',
            '_token': 'vmfkkQnXY13pyBnPnIj6R0dVtIfwOykUXDDohXDA',
        },
    },
    'PIKIRAN-RAKYAT': {
        'NAME': 'Pikiran Rakyat',
        'START': 'https://www.pikiran-rakyat.com/api/articles?limit=10&page=%s',
        'ARTICLES': '/',
        'NEXT_PAGES': '/',
        'TITLE': '//article/h1[1]//text()',
        'AUTHOR': '//article//small[@class="text-muted"][1]//text()',
        'DATE': '//article//small[@class="text-muted"][2]//text()',
        'TAG': '//div[@class="tag rounded mt-3"]/ul/li//text()',
        'CATEGORY': '//a[@class="btn active btn-secondary btn-sm"]/text()',
        'CONTENTS': '//div[@id="content-article"]//text()',
    },
        'JAKARTAPOST': {
        'NAME': 'Jakarta Post',
        'START': 'https://www.thejakartapost.com/news/index',
        'ARTICLES': '//div[@class="newsWord"]/a[2]/@href',
        'NEXT_PAGES': '//div[@class="navigation-page"]/a/@href',
        'TITLE': '//h1[@class="title-large"]/text()',
        'AUTHOR': '//span[@class="name-post"]/text()',
        'DATE': '//span[@class="day"]/text()',
        'TAG': '//div[@class="topicRelated"]/ul/li/a/text()',
        'CATEGORY': '//a[@class="dt-news"]/text()',
        'CONTENTS': '//div[@class="col-md-10 col-xs-12 detailNews"]//text()',
        'STOP_CRITERION': r'Topics :',
    },
        'METROTVNEWS': {
        'NAME': 'Metrotvnews',
        'START': 'http://www.metrotvnews.com/index/%s',
        'ARTICLES': '//ul/li/h2/a/@href',
        'NEXT_PAGES': '/',
        'TITLE': '//div[@class="detail"]/h1/text()',
        'AUTHOR': '//div[@class="reg"]/text()',
        'DATE': '//div[@class="reg"]/text()',
        'TAG': '//div[@class="line"]/a/text()',
        'CATEGORY': '//div[@class="breadcrumbs"]/a[2]/text()',
        'CONTENTS': '//div[@class="page"]//text()',
        'EXCLUDE_LINK': '//div[@class="related"]//text() || //div[@class="page"]//script/text()',
        'EXCLUDE_TEXT': r'.*Video.*',
        'STOP_CRITERION': r'\(\S+\)'
    },
    'USER_AGENT': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0",
    'ALLOWED_DOMAIN': [
        'www.tribunnews.com',
        'news.detik.com',
        'kompas.com',
        'tempo.co',
        'www.cnnindonesia.com',
        'republika.co.id',
        'sindonews.com',
        'liputan6.com',
        'www.beritasatu.com',
        'bisnis.com',
        'mediaindonesia.com',
        'antaranews.com',
        'okezone.com',
        'viva.co.id',
        'www.pikiran-rakyat.com',
        'www.thejakartapost.com',
        'metrotvnews.com'
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
