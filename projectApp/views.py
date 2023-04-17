from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
import tempfile
from django.conf import settings

# from puppeteer_pdf import render_pdf


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, 'test.html')

@csrf_exempt
def contact(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # message = request.POST.get('message')
        domain = request.POST.get('domain')
        print(name)
        print(email)
        # print(message)
        print(domain)
        origin = request.META.get('HTTP_ORIGIN')
        print(origin)

        allowed_domains = ['https://lifewithlg.com', 'https://www.example.com']

        if origin not in allowed_domains:
            return JsonResponse({'error': 'Invalid Origin'}, status=403)
        
        
        # save the data to the database
        # ...

        # return a JSON response with a success message

        # return a JSON response with the 'Access-Control-Allow-Origin' header
        response = JsonResponse({'message': 'Your message has been sent successfully!'})
        response['Access-Control-Allow-Origin'] = origin
        return response

    # return a 405 Method Not Allowed response for other HTTP methods
    return JsonResponse({'error': 'Method Not Allowed'}, status=405)


def generate_pdf(request):
    data = {'count': {'pages_404': 0,
  'pages_4xx': 0,
  'pages_500': 0,
  'pages_5xx': 0,
  'timed_out': 0,
  'h1_missing': 2,
  'title_long': 0,
  'title_short': 11,
  'noindex_page': 7,
  'redirect_302': 0,
  'redirect_3XX': 0,
  'multi_h1_tags': 8,
  'nofollow_page': 1,
  'redirect_loop': 0,
  'title_missing': 0,
  'meta_desc_long': 0,
  'redirect_chain': 0,
  'broken_redirect': 0,
  'meta_desc_short': 2,
  'og_tags_missing': 3,
  'multi_title_tags': 0,
  'image_alt_missing': 102,
  'meta_desc_missing': 4,
  'og_tags_incomplete': 9,
  'double_slash_in_url': 0,
  'follow_noindex_page': 7,
  'page_403_in_sitemap': 0,
  'page_4XX_in_sitemap': 0,
  'page_5XX_in_sitemap': 0,
  'multi_meta_desc_tags': 0,
  'twitter_card_missing': 3,
  'noindex_nofollow_page': 1,
  'redirect_HTTPS_to_HTTP': 0,
  'redirect_HTTP_to_HTTPS': 0,
  'canonical_points_to_4XX': 0,
  'canonical_points_to_5XX': 0,
  'noindex_page_in_sitemap': 0,
  'redirect_3XX_in_sitemap': 0,
  'redirect_chain_too_long': 0,
  'twitter_card_incomplete': 9,
  'HTTPS_HTTP_mixed_content': 0,
  'page_has_links_to_broken': 0,
  'page_has_links_to_redirect': 0,
  'page_has_no_outgoing_links': 2,
  'page_from_sitemap_timed_out': 0,
  'canonical_points_to_redirect': 0,
  'HTTPS_page_internal_link_HTTP': 0,
  'HTTP_page_internal_link_HTTPS': 0,
  'non_canonical_page_in_sitemap': 0,
  'og_URL_not_matching_canonical': 0,
  'HTTPS_page_links_to_HTTP_image': 0,
  'noncanonical_specified_as_canonical': 0,
  'page_has_nofollow_outgoing_internal': 0,
  'page_has_only_one_dofollow_incoming': 0,
  'orphan_page_has_no_incoming_internal_links': 0,
  'canonical_URL_has_no_incoming_internal_links': 12,
  'page_has_nofollow_dofollow_incoming_internals': 0,
  'page_has_nofollow_incoming_internal_links_only': 0,
  'redirected_page_has_no_incoming_internal_links': 0},
 'pages_404': {},
 'pages_4xx': {},
 'pages_500': {},
 'pages_5xx': {},
 'timed_out': {},
 'crawl_time': '2023-04-03 05:41:54',
 'h1_missing': {'0': ['https://app.tistasoft.com', 'Tistasoft'],
  '1': ['https://app.tistasoft.com/seoaudit/audit-site', 'Tistasoft']},
 'title_long': {},
 'title_short': {'0': ['https://tistasoft.com', 'Home - Tistasoft', 16],
  '1': ['https://app.tistasoft.com', 'Tistasoft', 9],
  '2': ['https://app.tistasoft.com/seoaudit/audit-site', 'Tistasoft', 9],
  '3': ['https://tistasoft.com/contact/', 'Contact - Tistasoft', 19],
  '4': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   'Email Protection | Cloudflare',
   29],
  '5': ['https://tistasoft.com/our-services/', 'Our Services - Tistasoft', 24],
  '6': ['https://tistasoft.com/our-approach/', 'Our Approach - Tistasoft', 24],
  '7': ['https://tistasoft.com/blog/', 'Blog - Tistasoft', 16],
  '8': ['https://tistasoft.com/category/featured/',
   'Featured - Tistasoft',
   20],
  '9': ['https://tistasoft.com/category/seo/', 'SEO - Tistasoft', 15],
  '10': ['https://tistasoft.com/author/editor/', 'editor - Tistasoft', 18]},
 'noindex_page': {'0': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   'Email Protection | Cloudflare'],
  '1': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword/',
   'Twitter DM Search Lets You Find Messages By Keyword - Tistasoft'],
  '2': ['https://tistasoft.com/featured/new-google-algorithm-update-aimed-at-product-reviews/',
   'New Google Algorithm Update Aimed At Product Reviews - Tistasoft'],
  '3': ['https://tistasoft.com/featured/new-integration-for-ga4-and-search-ads-360/',
   'New Integration For GA4 And Search Ads 360 - Tistasoft'],
  '4': ['https://tistasoft.com/seo/new-google-algorithm-update-aimed-at-product-reviews-2/',
   'New Google Algorithm Update Aimed At Product Reviews - Tistasoft'],
  '5': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword-2/',
   'Twitter DM Search Lets You Find Messages By Keyword - Tistasoft'],
  '6': ['https://tistasoft.com/author/editor/', 'editor - Tistasoft']},
 'redirect_302': {},
 'redirect_3XX': {},
 'multi_h1_tags': {'0': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword/',
   'Twitter DM Search Lets You Find Messages By Keyword',
   2],
  '1': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword/',
   'Solverwp- WordPress Theme and Plugin',
   2],
  '2': ['https://tistasoft.com/featured/new-google-algorithm-update-aimed-at-product-reviews/',
   'New Google Algorithm Update Aimed At Product Reviews',
   2],
  '3': ['https://tistasoft.com/featured/new-google-algorithm-update-aimed-at-product-reviews/',
   'Solverwp- WordPress Theme and Plugin',
   2],
  '4': ['https://tistasoft.com/featured/new-integration-for-ga4-and-search-ads-360/',
   'New Integration For GA4 And Search Ads 360',
   2],
  '5': ['https://tistasoft.com/featured/new-integration-for-ga4-and-search-ads-360/',
   'Solverwp- WordPress Theme and Plugin',
   2],
  '6': ['https://tistasoft.com/seo/new-google-algorithm-update-aimed-at-product-reviews-2/',
   'New Google Algorithm Update Aimed At Product Reviews',
   2],
  '7': ['https://tistasoft.com/seo/new-google-algorithm-update-aimed-at-product-reviews-2/',
   'Solverwp- WordPress Theme and Plugin',
   2],
  '8': ['https://tistasoft.com/category/featured/', 'Category: Featured', 2],
  '9': ['https://tistasoft.com/category/featured/',
   'Solverwp- WordPress Theme and Plugin',
   2],
  '10': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword-2/',
   'Twitter DM Search Lets You Find Messages By Keyword',
   2],
  '11': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword-2/',
   'Solverwp- WordPress Theme and Plugin',
   2],
  '12': ['https://tistasoft.com/category/seo/', 'Category: SEO', 2],
  '13': ['https://tistasoft.com/category/seo/',
   'Solverwp- WordPress Theme and Plugin',
   2],
  '14': ['https://tistasoft.com/author/editor/', 'Author: editor', 2],
  '15': ['https://tistasoft.com/author/editor/',
   'Solverwp- WordPress Theme and Plugin',
   2]},
 'nofollow_page': {'0': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   'Email Protection | Cloudflare']},
 'redirect_loop': {},
 'title_missing': {},
 'meta_desc_long': {},
 'redirect_chain': {},
 'broken_redirect': {},
 'meta_desc_short': {'0': ['https://tistasoft.com/our-services/',
   'Search Engine Optimization',
   26],
  '1': ['https://tistasoft.com/blog/', 'Featured', 8]},
 'og_tags_missing': {'0': ['https://app.tistasoft.com', 'Tistasoft'],
  '1': ['https://app.tistasoft.com/seoaudit/audit-site', 'Tistasoft'],
  '2': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   'Email Protection | Cloudflare']},
 'multi_title_tags': {},
 'image_alt_missing': {'0': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '1': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/02/6-piller.png'],
  '2': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/02/Scaling-an-SEO-Agency-1024x1024.png'],
  '3': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/02/Scaling-an-SEO-Agency.png'],
  '4': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/02/An-In-depth-Technical.png'],
  '5': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/02/An-In-depth-Technical.png'],
  '6': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/04/Daily-KW-Rank-Tracking.png'],
  '7': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/Client-Reporting.png'],
  '8': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/client-onboard.png'],
  '9': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/campaign-setup-1.png'],
  '10': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/regular-activities1.png'],
  '11': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/performance-tracking1.png'],
  '12': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/monthly-auto-reporting1.png'],
  '13': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/review-refine1.png'],
  '14': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/client-onboard.png'],
  '15': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/campaign-setup-1.png'],
  '16': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/regular-activities1.png'],
  '17': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/performance-tracking1.png'],
  '18': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/monthly-auto-reporting1.png'],
  '19': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/03/review-refine1.png'],
  '20': ['https://tistasoft.com',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '21': ['https://tistasoft.com/contact/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '22': ['https://tistasoft.com/contact/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '23': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '24': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Search-Engine-Optimization.png'],
  '25': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Content-Marketing.png'],
  '26': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Lead-Generation.png'],
  '27': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Email-Marketing.png'],
  '28': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Linkedin-Marketing.png'],
  '29': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Social-Media-Marketing.png'],
  '30': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Parformance-Marketing.png'],
  '31': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Revenu-Optimization.png'],
  '32': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Search-Engine-Optimization.png'],
  '33': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Content-Marketing.png'],
  '34': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Lead-Generation.png'],
  '35': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Email-Marketing.png'],
  '36': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Linkedin-Marketing.png'],
  '37': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Social-Media-Marketing.png'],
  '38': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Parformance-Marketing.png'],
  '39': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/08/Revenu-Optimization.png'],
  '40': ['https://tistasoft.com/our-services/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '41': ['https://tistasoft.com/our-approach/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '42': ['https://tistasoft.com/our-approach/',
   'https://tistasoft.com/wp-content/uploads/2022/04/video-Screen.jpg'],
  '43': ['https://tistasoft.com/our-approach/',
   'https://tistasoft.com/wp-content/uploads/2022/04/video-Screen.jpg'],
  '44': ['https://tistasoft.com/our-approach/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '45': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '46': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '47': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '48': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1.png'],
  '49': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '50': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '51': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/ga4-search-ads-360-623b7f13489f5-sej-1520x800-1-1024x539.png'],
  '52': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/ga4-search-ads-360-623b7f13489f5-sej-1520x800-1.png'],
  '53': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '54': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '55': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '56': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1.png'],
  '57': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '58': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '59': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '60': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/ga4-search-ads-360-623b7f13489f5-sej-1520x800-1-1024x539.png'],
  '61': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '62': ['https://tistasoft.com/blog/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '63': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '64': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '65': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '66': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '67': ['https://tistasoft.com/featured/new-google-algorithm-update-aimed-at-product-reviews/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '68': ['https://tistasoft.com/featured/new-google-algorithm-update-aimed-at-product-reviews/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '69': ['https://tistasoft.com/featured/new-google-algorithm-update-aimed-at-product-reviews/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '70': ['https://tistasoft.com/featured/new-google-algorithm-update-aimed-at-product-reviews/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '71': ['https://tistasoft.com/featured/new-integration-for-ga4-and-search-ads-360/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '72': ['https://tistasoft.com/featured/new-integration-for-ga4-and-search-ads-360/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '73': ['https://tistasoft.com/featured/new-integration-for-ga4-and-search-ads-360/',
   'https://tistasoft.com/wp-content/uploads/2022/03/ga4-search-ads-360-623b7f13489f5-sej-1520x800-1-1024x539.png'],
  '74': ['https://tistasoft.com/featured/new-integration-for-ga4-and-search-ads-360/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '75': ['https://tistasoft.com/seo/new-google-algorithm-update-aimed-at-product-reviews-2/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '76': ['https://tistasoft.com/seo/new-google-algorithm-update-aimed-at-product-reviews-2/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '77': ['https://tistasoft.com/seo/new-google-algorithm-update-aimed-at-product-reviews-2/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '78': ['https://tistasoft.com/seo/new-google-algorithm-update-aimed-at-product-reviews-2/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '79': ['https://tistasoft.com/category/featured/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '80': ['https://tistasoft.com/category/featured/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '81': ['https://tistasoft.com/category/featured/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '82': ['https://tistasoft.com/category/featured/',
   'https://tistasoft.com/wp-content/uploads/2022/03/ga4-search-ads-360-623b7f13489f5-sej-1520x800-1-1024x539.png'],
  '83': ['https://tistasoft.com/category/featured/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '84': ['https://tistasoft.com/category/featured/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '85': ['https://tistasoft.com/category/featured/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '86': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword-2/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '87': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword-2/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '88': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword-2/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '89': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword-2/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '90': ['https://tistasoft.com/category/seo/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '91': ['https://tistasoft.com/category/seo/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '92': ['https://tistasoft.com/category/seo/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '93': ['https://tistasoft.com/category/seo/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png'],
  '94': ['https://tistasoft.com/author/editor/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '95': ['https://tistasoft.com/author/editor/',
   'https://tistasoft.com/wp-content/uploads/2022/05/header-logo-hover.jpg'],
  '96': ['https://tistasoft.com/author/editor/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '97': ['https://tistasoft.com/author/editor/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '98': ['https://tistasoft.com/author/editor/',
   'https://tistasoft.com/wp-content/uploads/2022/03/ga4-search-ads-360-623b7f13489f5-sej-1520x800-1-1024x539.png'],
  '99': ['https://tistasoft.com/author/editor/',
   'https://tistasoft.com/wp-content/uploads/2022/03/google-june-core-algorithm-update.jpeg'],
  '100': ['https://tistasoft.com/author/editor/',
   'https://tistasoft.com/wp-content/uploads/2022/03/twitter-search-dm-keyword-623c84059f324-sej-1520x800-1-1024x539.png'],
  '101': ['https://tistasoft.com/author/editor/',
   'https://tistasoft.com/wp-content/uploads/2022/02/header-logo.png']},
 'meta_desc_missing': {'0': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   200],
  '1': ['https://tistasoft.com/category/featured/', 200],
  '2': ['https://tistasoft.com/category/seo/', 200],
  '3': ['https://tistasoft.com/author/editor/', 200]},
 'og_tags_incomplete': {'0': ['https://tistasoft.com',
   'Home - Tistasoft',
   'https://tistasoft.com/'],
  '1': ['https://app.tistasoft.com', 'Tistasoft', ''],
  '2': ['https://app.tistasoft.com/seoaudit/audit-site', 'Tistasoft', ''],
  '3': ['https://tistasoft.com/contact/',
   'Contact - Tistasoft',
   'https://tistasoft.com/contact/'],
  '4': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   'Email Protection | Cloudflare',
   ''],
  '5': ['https://tistasoft.com/our-services/',
   'Our Services - Tistasoft',
   'https://tistasoft.com/our-services/'],
  '6': ['https://tistasoft.com/category/featured/',
   'Featured - Tistasoft',
   'https://tistasoft.com/category/featured/'],
  '7': ['https://tistasoft.com/category/seo/',
   'SEO - Tistasoft',
   'https://tistasoft.com/category/seo/'],
  '8': ['https://tistasoft.com/author/editor/',
   'editor - Tistasoft',
   'https://tistasoft.com/author/editor/']},
 'double_slash_in_url': {},
 'follow_noindex_page': {'0': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   'Email Protection | Cloudflare'],
  '1': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword/',
   'Twitter DM Search Lets You Find Messages By Keyword - Tistasoft'],
  '2': ['https://tistasoft.com/featured/new-google-algorithm-update-aimed-at-product-reviews/',
   'New Google Algorithm Update Aimed At Product Reviews - Tistasoft'],
  '3': ['https://tistasoft.com/featured/new-integration-for-ga4-and-search-ads-360/',
   'New Integration For GA4 And Search Ads 360 - Tistasoft'],
  '4': ['https://tistasoft.com/seo/new-google-algorithm-update-aimed-at-product-reviews-2/',
   'New Google Algorithm Update Aimed At Product Reviews - Tistasoft'],
  '5': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword-2/',
   'Twitter DM Search Lets You Find Messages By Keyword - Tistasoft'],
  '6': ['https://tistasoft.com/author/editor/', 'editor - Tistasoft']},
 'page_403_in_sitemap': {},
 'page_4XX_in_sitemap': {},
 'page_5XX_in_sitemap': {},
 'multi_meta_desc_tags': {},
 'twitter_card_missing': {'0': ['https://app.tistasoft.com', 'Tistasoft'],
  '1': ['https://app.tistasoft.com/seoaudit/audit-site', 'Tistasoft'],
  '2': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   'Email Protection | Cloudflare']},
 'noindex_nofollow_page': {'0': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   'Email Protection | Cloudflare']},
 'redirect_HTTPS_to_HTTP': {},
 'redirect_HTTP_to_HTTPS': {},
 'canonical_points_to_4XX': {},
 'canonical_points_to_5XX': {},
 'noindex_page_in_sitemap': {},
 'redirect_3XX_in_sitemap': {},
 'redirect_chain_too_long': {},
 'twitter_card_incomplete': {'0': ['https://tistasoft.com',
   'Home - Tistasoft'],
  '1': ['https://app.tistasoft.com', 'Tistasoft'],
  '2': ['https://app.tistasoft.com/seoaudit/audit-site', 'Tistasoft'],
  '3': ['https://tistasoft.com/contact/', 'Contact - Tistasoft'],
  '4': ['https://tistasoft.com/cdn-cgi/l/email-protection',
   'Email Protection | Cloudflare'],
  '5': ['https://tistasoft.com/our-services/', 'Our Services - Tistasoft'],
  '6': ['https://tistasoft.com/category/featured/', 'Featured - Tistasoft'],
  '7': ['https://tistasoft.com/category/seo/', 'SEO - Tistasoft'],
  '8': ['https://tistasoft.com/author/editor/', 'editor - Tistasoft']},
 'HTTPS_HTTP_mixed_content': {},
 'page_has_links_to_broken': {},
 'page_has_links_to_redirect': {},
 'page_has_no_outgoing_links': {'0': ['https://app.tistasoft.com',
   'Tistasoft'],
  '1': ['https://app.tistasoft.com/seoaudit/audit-site', 'Tistasoft']},
 'page_from_sitemap_timed_out': {},
 'canonical_points_to_redirect': {},
 'HTTPS_page_internal_link_HTTP': {},
 'HTTP_page_internal_link_HTTPS': {},
 'non_canonical_page_in_sitemap': {},
 'og_URL_not_matching_canonical': {},
 'HTTPS_page_links_to_HTTP_image': {},
 'noncanonical_specified_as_canonical': {},
 'page_has_nofollow_outgoing_internal': {},
 'page_has_only_one_dofollow_incoming': {},
 'orphan_page_has_no_incoming_internal_links': {},
 'canonical_URL_has_no_incoming_internal_links': {'0': ['https://tistasoft.com'],
  '1': ['https://app.tistasoft.com'],
  '2': ['https://app.tistasoft.com/seoaudit/audit-site'],
  '3': ['https://tistasoft.com/cdn-cgi/l/email-protection'],
  '4': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword/'],
  '5': ['https://tistasoft.com/featured/new-google-algorithm-update-aimed-at-product-reviews/'],
  '6': ['https://tistasoft.com/featured/new-integration-for-ga4-and-search-ads-360/'],
  '7': ['https://tistasoft.com/seo/new-google-algorithm-update-aimed-at-product-reviews-2/'],
  '8': ['https://tistasoft.com/featured/twitter-dm-search-lets-you-find-messages-by-keyword-2/'],
  '9': ['https://tistasoft.com/author/editor/'],
  '10': ['https://tistasoft.com/'],
  '11': ['']},
 'page_has_nofollow_dofollow_incoming_internals': {},
 'page_has_nofollow_incoming_internal_links_only': {},
 'redirected_page_has_no_incoming_internal_links': {}}
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print("1")
    # Get the template and context data
    template = get_template('test.html')
    print("2")
    context = {'title': 'My PDF', 'domain': 'tistasoft.com', 'data': data, 'timeMarkerInSecond': 3, 'list': list}
    print("2")
    # Render the template with context data
    html = template.render(context)

    # Generate the PDF using WeasyPrint
    # pdf_file = HTML(string=html).write_pdf()
    pdf_file = HTML(string=html, base_url=settings.STATIC_URL).write_pdf()
    # pdf_file = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[settings.STATIC_ROOT + 'test.css'])

    # Save the PDF to a file path
    file_path = 'PDF/file1.pdf'
    with open(file_path, 'wb') as f:
        f.write(pdf_file)

    # Return a response to download the PDF
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="my_file.pdf"'
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'test.html', context)


# def download_pdf(request):
#     pdf_file = render_pdf(request, template_name='path/to/test.html')
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="my_pdf.pdf"'
#     return response


# def pdf_generation(request):
#     html_template = get_template('templates/home_page.html')
#     pdf_file = HTML(string=html_template).write_pdf()
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="home_page.pdf"'
#     return HttpResponse("Hello, world. You're at the polls index.")

# def get_generated_problems_in_pdf(request):

#     # queryset
#     # problems = Problem.objects.all()
#     problems = {"category": 'a',
#                 "description": 'b',
#                 "problem_id": 'c',
#                 "breakdown": 'd'
#                 }

#     # context passed in the template
#     context = {'problems': problems}

#     # render
#     html_string = render_to_string(
#         'templates/problems.html',context)
#     html = HTML(string=html_string)
#     result = html.write_pdf()

#     # http response
#     response = HttpResponse(content_type='application/pdf;')
#     response['Content-Disposition'] = 'inline; filename=problem_list.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'
#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()
#         output = open(output.name, 'rb')
#         response.write(output.read())

#     return response