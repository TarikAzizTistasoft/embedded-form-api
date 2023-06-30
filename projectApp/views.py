import datetime
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import datetime as dt

from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
import tempfile
from django.conf import settings
from xhtml2pdf import pisa

from django.views.generic import View

from projectApp.utils import render_to_pdf

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

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # data = {
        #      'today': datetime.date.today(), 
        #      'amount': 39.99,
        #     'customer_name': 'Cooper Mann',
        #     'order_id': 1233434,
        # }
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
         'redirected_page_has_no_incoming_internal_links': 0}}
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        context = {'title': 'My PDF', 'domain': 'tistasoft.com', 'data': data, 'timeMarkerInSecond': 3, 'list': list}

        # pdf = render_to_pdf('pdf/invoice.html', data)
        pdf=render_to_pdf('pdf/test.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

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
    reporting_time = dt.datetime.today().strftime("%B %d, %Y")
    issues = {
    "category": [
        {
            "id": 1,
            "title": "INTERNAL PAGES",
            "order": 1,
            "created_date": "2023-05-02T13:33:44Z",
            "deleted_date": 'null'
        },
        {
            "id": 2,
            "title": "CONTENT",
            "order": 2,
            "created_date": "2023-05-02T13:39:16Z",
            "deleted_date": 'null'
        },
        {
            "id": 3,
            "title": "INDEXABILITY",
            "order": 3,
            "created_date": "2023-05-02T15:50:02Z",
            "deleted_date": 'null'
        },
        {
            "id": 4,
            "title": "BACKLINKS",
            "order": 4,
            "created_date": "2023-05-02T16:30:01Z",
            "deleted_date": 'null'
        },
        {
            "id": 5,
            "title": "BACKLINK REDIRECTS",
            "order": 5,
            "created_date": "2023-05-02T16:47:09Z",
            "deleted_date": 'null'
        },
        {
            "id": 6,
            "title": "SOCIAL TAGs",
            "order": 6,
            "created_date": "2023-05-02T17:03:25Z",
            "deleted_date": 'null'
        },
        {
            "id": 7,
            "title": "IMAGES",
            "order": 7,
            "created_date": "2023-05-02T17:23:15Z",
            "deleted_date": 'null'
        },
        {
            "id": 8,
            "title": "OTHERS",
            "order": 8,
            "created_date": "2023-05-02T17:26:42Z",
            "deleted_date": 'null'
        }
    ],
    "subcategory": [
        {
            "id": 17,
            "title": "Canonical points to 4xx",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "canonical_points_to_4XX",
            "excel_tab": "canonical_points_to_4XX",
            "order": 1,
            "is_visible": 'true',
            "created_date": "2023-05-02T15:50:41Z",
            "deleted_date": 'null',
            "parentcategory": 3
        },
        {
            "id": 18,
            "title": "Canonical points to 5xx",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "canonical_points_to_5XX",
            "excel_tab": "canonical_points_to_5XX",
            "order": 2,
            "is_visible": 'true',
            "created_date": "2023-05-02T15:54:39Z",
            "deleted_date": 'null',
            "parentcategory": 3
        },
        {
            "id": 19,
            "title": "Canonical points to redirect",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "canonical_points_to_redirect",
            "excel_tab": "canonical_points_to_redirect",
            "order": 3,
            "is_visible": 'true',
            "created_date": "2023-05-02T15:55:09Z",
            "deleted_date": 'null',
            "parentcategory": 3
        },
        {
            "id": 20,
            "title": "Nofollow Page",
            "issue_type": 1,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "nofollow_page",
            "excel_tab": "nofollow_page",
            "order": 4,
            "is_visible": 'true',
            "created_date": "2023-05-02T15:55:46Z",
            "deleted_date": 'null',
            "parentcategory": 3
        },
        {
            "id": 22,
            "title": "Non-canonical page specified as canonical one",
            "issue_type": 1,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "noncanonical_specified_as_canonical",
            "excel_tab": "noncanonical_specified_as_canon",
            "order": 6,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:25:18Z",
            "deleted_date": 'null',
            "parentcategory": 3
        },
        {
            "id": 23,
            "title": "Noindex and nofollow page",
            "issue_type": 2,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "noindex_nofollow_page",
            "excel_tab": "noindex_nofollow_page",
            "order": 7,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:27:03Z",
            "deleted_date": 'null',
            "parentcategory": 3
        },
        {
            "id": 25,
            "title": "Canonical URL&nbsp;&nbsp; has no incoming internal links",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "canonical_URL_has_no_incoming_internal_links",
            "excel_tab": "canonical_URL_has_no_incoming_i",
            "order": 1,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:30:55Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 26,
            "title": "HTTPS&nbsp;&nbsp; page has internal link to HTTP",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "HTTPS_page_internal_link_HTTP",
            "excel_tab": "HTTPS_page_internal_link_HTTP",
            "order": 2,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:31:51Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 33,
            "title": "HTTP&nbsp;&nbsp; page has internal links to HTTPS",
            "issue_type": 2,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "HTTP_page_internal_link_HTTPS",
            "excel_tab": "HTTP_page_internal_link_HTTPS",
            "order": 9,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:41:24Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 35,
            "title": "page has nofollow outgoing internal links",
            "issue_type": 2,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "page_has_nofollow_outgoing_internal",
            "excel_tab": "page_has_nofollow_outgoing_inte",
            "order": 11,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:44:19Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 36,
            "title": "Page has only one dofollow incoming internal link",
            "issue_type": 2,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "page_has_only_one_dofollow_incoming",
            "excel_tab": "page_has_only_one_dofollow_inco",
            "order": 12,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:44:51Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 38,
            "title": "Redirect chain too long",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "redirect_chain_too_long",
            "excel_tab": "redirect_chain_too_long",
            "order": 2,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:51:37Z",
            "deleted_date": 'null',
            "parentcategory": 5
        },
        {
            "id": 43,
            "title": "HTTPS&nbsp;&nbsp; to HTTP&nbsp;&nbsp; redirect",
            "issue_type": 1,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "redirect_HTTPS_to_HTTP",
            "excel_tab": "redirect_HTTPS_to_HTTP",
            "order": 7,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:59:52Z",
            "deleted_date": 'null',
            "parentcategory": 5
        },
        {
            "id": 44,
            "title": "HTTP&nbsp;&nbsp; to HTTPS&nbsp;&nbsp; redirect",
            "issue_type": 2,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "redirect_HTTP_to_HTTPS",
            "excel_tab": "redirect_HTTP_to_HTTPS",
            "order": 8,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:00:49Z",
            "deleted_date": 'null',
            "parentcategory": 5
        },
        {
            "id": 45,
            "title": "Open Graph URL&nbsp;&nbsp; not matching canonical",
            "issue_type": 1,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "og_URL_not_matching_canonical",
            "excel_tab": "og_URL_not_matching_canonical",
            "order": 1,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:04:14Z",
            "deleted_date": 'null',
            "parentcategory": 6
        },
        {
            "id": 47,
            "title": "Twitter card incomplete",
            "issue_type": 1,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "twitter_card_incomplete",
            "excel_tab": "twitter_card_incomplete",
            "order": 3,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:17:53Z",
            "deleted_date": 'null',
            "parentcategory": 6
        },
        {
            "id": 49,
            "title": "Twitter card missing",
            "issue_type": 2,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "twitter_card_missing",
            "excel_tab": "twitter_card_missing",
            "order": 5,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:19:22Z",
            "deleted_date": 'null',
            "parentcategory": 6
        },
        {
            "id": 53,
            "title": "403 page in sitemap",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "page_403_in_sitemap",
            "excel_tab": "page_403_in_sitemap",
            "order": 2,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:28:16Z",
            "deleted_date": 'null',
            "parentcategory": 8
        },
        {
            "id": 54,
            "title": "4XX page in sitemap",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "page_4XX_in_sitemap",
            "excel_tab": "page_4XX_in_sitemap",
            "order": 3,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:28:43Z",
            "deleted_date": 'null',
            "parentcategory": 8
        },
        {
            "id": 55,
            "title": "5XX page in sitemap",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "page_5XX_in_sitemap",
            "excel_tab": "page_5XX_in_sitemap",
            "order": 4,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:29:36Z",
            "deleted_date": 'null',
            "parentcategory": 8
        },
        {
            "id": 59,
            "title": "Page from sitemap timed out",
            "issue_type": 0,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "page_from_sitemap_timed_out",
            "excel_tab": "page_from_sitemap_timed_out",
            "order": 8,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:32:05Z",
            "deleted_date": 'null',
            "parentcategory": 8
        },
        {
            "id": 3,
            "title": "500 page",
            "issue_type": 0,
            "description": "URLs that return the 500 HTTP status code (Internal Server Error).\r\n\r\nThis code indicates a potential problem with your web server.\r\n\r\nThese URLs can be accessed neither by your website visitors nor by the search engines crawlers. Crawlers will be forced to abandon the request while people will most likely leave your website.",
            "risk": "",
            "how_to_fix": "Review the list of URLs that return 500 HTTP status code.\r\n\r\nTry to reproduce the server error reported by Site Audit for these URLs in your browser. You should also check the error logs for your server. If this is an ongoing problem and a lot of internal pages return 5xx code, you need to check with your hosting provider or with your web developers.\r\n\r\nYou should also note that this can be a temporary issue, e.g., when the crawl took place during some maintenance on your website's server.",
            "more_details": "",
            "data_key": "pages_500",
            "excel_tab": "pages_500",
            "order": 3,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:36:50Z",
            "deleted_date": 'null',
            "parentcategory": 1
        },
        {
            "id": 31,
            "title": "Page has nofollow incoming internal links only",
            "issue_type": 1,
            "description": "Search engine bots won't be able to crawl (and thus index) the affected pages via nofollowed links.\r\n\r\nBesides, no link equity will be passed to the linked pages via nofollowed links.",
            "risk": "\"\"Nofollow\"\" links should only point to the specific pages that are no desired to be ranked on Google.\r\nIf pages desired to rank on Google must have good number of relevant \"\"followed\"\" internal links from other pages on the website.",
            "how_to_fix": "Review the list of URLs mentioned in the sheet and corerct all of them by remoing the \"NoFollow\" tag. Also \"NoIndex\" tag if present.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} pages which are linked from different pages with \"NoFollow\" internal links e.g. ${data[subcategory.data_key][0][0]} has been linked from ${data['count'][subcategory.data_key]} internal links which are marked \"NoFollow\". For complete reference of affected URLs, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "page_has_nofollow_incoming_internal_links_only",
            "excel_tab": "page_has_nofollow_incoming_inte",
            "order": 7,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:39:52Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 41,
            "title": "3XX&nbsp;&nbsp; Redirect",
            "issue_type": 1,
            "description": "Even though Google announced that any redirection method is good and will pass PageRank, Googlebot is not the only visitor of your website.",
            "risk": "Redirects always require caution. They may hurt your website performance, especially for mobile users, or confuse website visitors.",
            "how_to_fix": "It is recommended to replace the links to the internal redirected URLs on your website with the direct links to the destination pages where possible.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} internal URL redirects .The URL ${data[subcategory.data_key][0][0]} is redirected to ${data[subcategory.data_key][0][1]}. It is advisable to link to the target URL directly. \r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "redirect_3XX",
            "excel_tab": "redirect_3XX",
            "order": 5,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:55:00Z",
            "deleted_date": 'null',
            "parentcategory": 5
        },
        {
            "id": 58,
            "title": "Non-canonical page in sitemap",
            "issue_type": 0,
            "description": "Non-canonical pages listed in the sitemap. If the page is canonical to other page, no need to include concerned page in sitemap.xml then.",
            "risk": "Sitemap files must list the pages you want search engines to crawl and index. All pages listed in a sitemap are suggested as canonicals for the search engines.",
            "how_to_fix": "Make sure your sitemap only includes canonical URLs. Either exclude these URLs from sitemap.xml or appropriately correct the canonical URLs.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs that are canonical to other URL but included in the sitemap.xml for indexation. An example URL is ${data[subcategory.data_key][0][0]} is canonical to ${data[subcategory.data_key][0][1]}; not itself.For complete list, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "non_canonical_page_in_sitemap",
            "excel_tab": "non_canonical_page_in_sitemap",
            "order": 7,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:31:36Z",
            "deleted_date": 'null',
            "parentcategory": 8
        },
        {
            "id": 8,
            "title": "Multiple title tags",
            "issue_type": 0,
            "description": "Pages with more than one <title> tag.\r\n\r\nAlthough multiple title tags probably wouldn't cause problems for Google today, this is always a confusion because only one title will be picked to be displayed in the search results and in the browser's tab.\r\n\r\nBesides, multiple title tags are a relic of old black-hat SEO and won't add authority to your pages.",
            "risk": "",
            "how_to_fix": "You might need help from your developer to understand why your pages have more than one title tag.\r\n\r\nPick only one unique descriptive title for each page and make the necessary edits to the page code.",
            "more_details": "",
            "data_key": "multi_title_tags",
            "excel_tab": "multi_title_tags",
            "order": 2,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:40:45Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 10,
            "title": "H1&nbsp;&nbsp; tag missing or empty",
            "issue_type": 1,
            "description": "<h1> tag is the top level heading of the page. Although it is not as crucial as your page title, an <h1> heading is a strong component of your on-page SEO. It helps search engines better understand the content on your page and its overall topic.",
            "risk": "A missing title tag is a huge opportunity loss for your page to rank for desired keywords.",
            "how_to_fix": "Each page should have its unique <h1> heading.\r\nIt is recommended to use only one <h1> tag per page.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs that has longer than desired title tag. An example URL is ${data[subcategory.data_key][0][0]} has no H1 tag. For a complete list, refer to the tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "h1_missing",
            "excel_tab": "h1_missing",
            "order": 4,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:41:51Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 11,
            "title": "Meta description tag missing or empty",
            "issue_type": 1,
            "description": "Pages that have an empty or missing Meta description tag.\r\nWithout a Meta description, you're missing the opportunity to present the summary of your page content to the search engines. High-quality descriptions can sometimes be displayed in Google's search results as search snippets.\r\nMeta description is the most important SEO tag after Meta title.",
            "risk": "A well described Meta description is an opportunity to present the summary of the page content to the search engines. High quality descriptions can sometimes be displayed in Google's search results as search snippets.",
            "how_to_fix": "You should provide a unique Meta description for each index-able page on your website to help search engines and people quickly understand what your page is about.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs without a Meta description tag. An example URL is ${data[subcategory.data_key][0][0]} has no Meta description tag filled up. For a complete list, refer to the tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "meta_desc_missing",
            "excel_tab": "meta_desc_missing",
            "order": 5,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:42:19Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 12,
            "title": "Meta description too long",
            "issue_type": 1,
            "description": "Google sometimes uses <meta> tag content to generate snippets, if they think they give users a more accurate description than can be taken directly from the page content.\r\n\r\nBesides, Facebook, for example, will use <meta> tag content for link preview if the page has no 'og:description' tag.",
            "risk": "If Google decides to use the page meta description as a snippet, a long one can be truncated.",
            "how_to_fix": "A general recommendation today is to keep your page description between 110 and 160 characters, although Google can sometimes show longer snippets.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs that have longer than desired Meta description. An example URL is ${data[subcategory.data_key][0][0]} has Meta description of length ${data[subcategory.data_key][0][2]}. For a complete list, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "meta_desc_long",
            "excel_tab": "meta_desc_long",
            "order": 6,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:42:42Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 13,
            "title": "Meta description too short",
            "issue_type": 1,
            "description": "Google sometimes uses <meta> tag content to generate snippets, if they think they give users a more accurate description than can be taken directly from the page content.\r\n\r\nBesides, Facebook, for example, will use <meta> tag content for link preview if the page has no 'og:description' tag.",
            "risk": "A short meta description may not summarize the content of your page in the best possible way.",
            "how_to_fix": "A general recommendation today is to keep your page description between 110 and 160 characters, although Google can sometimes show longer snippets.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs that have longer than desired title tag. An example URL is ${data[subcategory.data_key][0][0]} has Meta description of length ${data[subcategory.data_key][0][2]}. For a complete list, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "meta_desc_short",
            "excel_tab": "meta_desc_short",
            "order": 7,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:43:16Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 14,
            "title": "Title too long",
            "issue_type": 1,
            "description": "Longer titles will be truncated when they show up in the search results.",
            "risk": "Poor user experience, lower click-through rate (CTR), negative SEO.",
            "how_to_fix": "Generally, recommended title length is between 50 and 60 characters (max 600 pixels).\r\n\r\nReview all the pages reported and consider shortening their titles.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs that have longer than desired title tag. An example URL is ${data[subcategory.data_key][0][0]} has title of length ${data[subcategory.data_key][0][2]}. For a complete list, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "title_long",
            "excel_tab": "title_long",
            "order": 8,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:43:45Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 9,
            "title": "Title tag missing or empty",
            "issue_type": 0,
            "description": "Pages with an empty or missing <title> tag.\r\n\r\nThe HTML <title> tag is a crucial component of on-page SEO.\r\n\r\nPage title will be displayed in search results and it will show up as a name of a browser's tab for those who visit your web page.",
            "risk": "Page title will be displayed in search results and it will show up as a name of a browser's tab for those who visit your web page.",
            "how_to_fix": "Review all the pages with missing or empty <title> tag in this report.\r\n\r\nAdd a concise title perfectly describing your page content, with your targeted keyword in mind, to every web page.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} URL i.e. ${data[subcategory.data_key][0][0]} without a title tag. For more details refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "title_missing",
            "excel_tab": "title_missing",
            "order": 3,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:41:21Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 16,
            "title": "Multiple H1&nbsp;&nbsp; tags",
            "issue_type": 2,
            "description": "Pages that have more than one <h1> tag.\r\n\r\nIt is possible to have multiple <h1> tags on your pages.\r\n\r\nJohn Mueller of Google mentioned that you could use as many <h1> tags on a page as you need, hinting that Google is smart enough to puzzle out your headers.",
            "risk": "It is advisable to provide single H1 to give clear signal regarding the content theme of the page.",
            "how_to_fix": "To avoid any possible confusion for search engines, you should consider keeping the recommended header hierarchy on all of your pages and use only one <h1> tag on a page.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} URLs that have multiple H1 tag. An example URL is ${data[subcategory.data_key][0][0]} has ${data[subcategory.data_key][0][2]} H1 tag. For a complete list, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "multi_h1_tags",
            "excel_tab": "multi_h1_tags",
            "order": 10,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:44:40Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 2,
            "title": "4XX page",
            "issue_type": 0,
            "description": "4xx HTTP status codes indicate that the requested page or resource cannot be accessed. 401 - Unauthorized, 403 - Forbidden, 408 - Request Timeout, and 404 - Not Found are the most common \"Client Errors\".\r\n\r\n4xx URLs damage the user experience on your website as people cannot access the page or file via a link they click. Besides, internal links to 4xx URLs create unnecessary \"dead ends\" for the search engine crawlers and can waste your crawl budget.\r\n\r\nPages of your website that changed their response code to 4xx will be removed from Google's index.",
            "risk": "",
            "how_to_fix": "Review the list of 4xx URLs. Click on the number of inlinks to a given 4xx URL to access the list of pages that link to it.\r\n\r\nYou should review the internal outgoing links to all the 4xx pages reported and either remove these links or replace them with relevant links to live pages.\r\n\r\nAlternatively, you can set the appropriate 301 redirects. It is especially important when for moved or deleted pages on your website.\r\n\r\nThis will provide smooth crawlability for your website and guarantee good user experience.\r\n\r\nThe HTTP 429 (Too Many Requests) response code may indicate that the crawling speed set in the crawl settings for your project is too high for a web server. Reduce it in the crawl settings and run a project re-crawl.",
            "more_details": "",
            "data_key": "pages_4xx",
            "excel_tab": "pages_4xx",
            "order": 2,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:36:26Z",
            "deleted_date": 'null',
            "parentcategory": 1
        },
        {
            "id": 4,
            "title": "5XX page",
            "issue_type": 0,
            "description": "URLs that return one of the 5xx HTTP status codes (Server Error).\r\n\r\nURLs return 5xx status codes when the server is not able to fulfill the request.\r\n\r\nThese URLs can be accessed neither by your website visitors nor by the search engines crawlers. Crawlers will be forced to abandon the request while people will most likely leave your website.",
            "risk": "",
            "how_to_fix": "Review the list of 5xx URLs.\r\n\r\nTry to reproduce the server error reported by the Site Audit for these URLs in your browser. You should also check the error logs for your server. If this is an ongoing problem and a lot of internal pages return 5xx code, you need to check with your hosting provider or with your web developers. Your server may be overloaded or misconfigured.\r\n\r\nYou should also note that this can be a temporary issue, e.g. when the crawl took place during some maintenance on your website's server.",
            "more_details": "",
            "data_key": "pages_5xx",
            "excel_tab": "pages_5xx",
            "order": 4,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:37:12Z",
            "deleted_date": 'null',
            "parentcategory": 1
        },
        {
            "id": 6,
            "title": "HTTPS&nbsp;&nbsp;/HTTP&nbsp;&nbsp; mixed content",
            "issue_type": 1,
            "description": "Mixed content occurs when initial HTML is loaded over a secure HTTPS connection, but resource files (images, CSS, or JS) are loaded over an insecure HTTP connection.\r\n\r\nA warning about this will be shown in modern browsers to inform users about the insecure resources on a page.\r\n\r\nMixed content degrades the security and user experience of your HTTPS site.",
            "risk": "",
            "how_to_fix": "Make sure all the resources on your web pages are loaded over a secure HTTPS connection.\r\n\r\nYou can find the resources linked via HTTP in the relevant columns of this report.\r\n\r\nIf the resource is available over HTTPS, you can simply link to its HTTPS version. Otherwise, you should:\r\n\r\nInclude the resource from a different host, if one is available.\r\nDownload and host the content on your site directly, if you are legally allowed to do so.\r\nExclude the resource from your site altogether.",
            "more_details": "",
            "data_key": "HTTPS_HTTP_mixed_content",
            "excel_tab": "HTTPS_HTTP_mixed_content",
            "order": 6,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:38:13Z",
            "deleted_date": 'null',
            "parentcategory": 1
        },
        {
            "id": 5,
            "title": "Timed out",
            "issue_type": 0,
            "description": "Response from the server was not received on time when requesting a page or resource.\r\n\r\nThis may damage your website crawlability (and thus indexability) and have a negative impact on the user experience.",
            "risk": "This may damage your website crawlability (and thus indexability) and have a negative impact on the user experience.",
            "how_to_fix": "Review the list of URLs that timed out.\r\n\r\nTry to reproduce the server error reported by Site Audit for these URLs in your browser. You should also check the error logs for your server. If this is an ongoing problem, you need to check with your hosting provider or with your web developers. Your server may be overloaded, misconfigured, or very slow.\r\n\r\nYou should also note that this can be a temporary issue, e.g. when the crawl took place during some maintenance on your website's server.",
            "more_details": "Google bot detected 37 URLs tha treceived \"Timed out\" . An example URL is https://www.horseland.com.au/gidgee-sunglass-strap-black/.For complete list, refer to tab sheet “Timed out”.",
            "data_key": "timed_out",
            "excel_tab": "timed_out",
            "order": 5,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:37:34Z",
            "deleted_date": 'null',
            "parentcategory": 1
        },
        {
            "id": 15,
            "title": "Title too short",
            "issue_type": 1,
            "description": "A short title may not describe the content of your page in the best possible way. \r\nIn absence of proper title, Google may even generate an improved title on its own from anchors, on-page text, or other sources for its SERP.",
            "risk": "A more descriptive title is always helpful to give a greater clarity of the page content to the user.",
            "how_to_fix": "Generally, recommended title length is between 50 and 70 characters (max 600 pixels). \r\n\r\nReview all the pages reported and consider writing longer titles.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs that have longer than desired title tag. An example URL is ${data[subcategory.data_key][0][0]} has title of length ${data[subcategory.data_key][0][2]}. For a complete list, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "title_short",
            "excel_tab": "title_short",
            "order": 9,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:44:11Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 29,
            "title": "Page has no outgoing links",
            "issue_type": 0,
            "description": "Site has pages that do not have any outgoing link internally or externally.",
            "risk": "Incomplete crawling by Google bot.",
            "how_to_fix": "Check your website navigation and link architecture to make sure your website has no \"dead ends.\"",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} URLs that links no outgoing links. An example URL is ${data[subcategory.data_key][0][0]} which has no outgoing links. \r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "page_has_no_outgoing_links",
            "excel_tab": "page_has_no_outgoing_links",
            "order": 5,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:33:57Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 1,
            "title": "404 page",
            "issue_type": 0,
            "description": "404 – Not Found is one of the most common 4xx errors and indicates that the requested URL does not exist.\r\n\r\nLinks pointing to the 404 URLs are widely known as \"broken links\".\r\n\r\n404 URLs on your website damage the user experience, as people cannot access the page or file via a link they click. Besides, internal links to 404 URLs create unnecessary \"dead ends\" for the search engine crawlers and can waste your crawl budget.",
            "risk": "404 URLs on your website damage the user experience, as people cannot access the page or file via a link they click. Besides, internal links to 404 URLs create unnecessary \"dead ends\" for the search engine crawlers and can waste your crawl budget.",
            "how_to_fix": "Review the list of 404 URLs on your website. Click on the number of inlinks to a given 404 URL to access the list of pages that link to it.\r\n\r\nYou should review the internal outgoing links to all the 404 pages reported and either remove these links or replace them with relevant links to live pages.\r\n\r\nAlternatively, you can set the appropriate 301 redirects. It is especially important for the 404 pages with a decent number of external backlinks.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} pages that return 404. For more details refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "pages_404",
            "excel_tab": "pages_404",
            "order": 1,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:35:46Z",
            "deleted_date": 'null',
            "parentcategory": 1
        },
        {
            "id": 7,
            "title": "Multiple Meta Description tags",
            "issue_type": 0,
            "description": "Pages that have more than one meta description tag.\r\n\r\nA meta description tag is generally used to inform the search engine with a short, informative summary of what your page is about. High-quality descriptions can sometimes be displayed in Google's search results as search snippets, helping you get higher click-through rates from SERPs.\r\n\r\nMultiple meta descriptions can confuse the search engines as they only expect one meta description tag per page.",
            "risk": "Multiple Meta descriptions can confuse the search engines as they only expect one Meta description tag per page.",
            "how_to_fix": "Review all the pages with multiple meta description tags listed in this report.\r\n\r\nPick the most informative and quality meta description for each page and remove the extra ones.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs with multiple Meta description tag. An example URL is  ${data[subcategory.data_key][0][0]} has ${data['count'][subcategory.data_key]} Meta description tag filled up .For complete list, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "multi_meta_desc_tags",
            "excel_tab": "multi_meta_desc_tags",
            "order": 1,
            "is_visible": 'true',
            "created_date": "2023-05-02T13:39:44Z",
            "deleted_date": 'null',
            "parentcategory": 2
        },
        {
            "id": 24,
            "title": "Noindex follow page",
            "issue_type": 2,
            "description": "Pages that have a 'noindex' but don't have a 'nofollow' tag in the HTML code or in the HTTP response header.",
            "risk": "\"Such pages will not be shown in search engines' results. But since they don't have a 'nofollow' tag, all links on them are supposed to be followed by search engine bots and pass \"\"link juice.\"\"\r\n\r\nHowever, in one of the recent Google Webmasters videos, Google’s John Mueller explained that Google will understand a long-term 'noindex' (without a 'nofollow') as a 'noindex, nofollow.'\"",
            "how_to_fix": "\"So, check this report for the 'noindex' pages you expect to pass link value to the other pages on your website.\r\n\r\nAnd if you want to make sure search engine bots won't follow the links on a 'noindex' page, add a 'nofollow' as a meta tag or as an HTTP response header.\"",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} Noindex follow page e.g. \r\n${data[subcategory.data_key][0][0]} is marked as NoINdex Follow page.  In the long run pages linked from these pages may not be followed. For more detailed refer to tab \"${subcategory.excel_tab}\"",
            "data_key": "follow_noindex_page",
            "excel_tab": "follow_noindex_page",
            "order": 8,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:27:35Z",
            "deleted_date": 'null',
            "parentcategory": 3
        },
        {
            "id": 21,
            "title": "Noindex page",
            "issue_type": 1,
            "description": "There are pages with \"NoIndex\" Meta tag blocking the pages from being indexed by Google.",
            "risk": "A 'noindex' meta tag is used on a page to prevent it from search indexing.",
            "how_to_fix": "\"Only use this tag on the pages you don't want to appear in search results.\r\n\r\nPlease take notice that for the noindex meta tag to be effective, the page must not be blocked by the robots.txt file. Otherwise, the search crawlers will not be able to see it.\r\n\r\nIf you want a page to be indexed by search engines, you should remove this tag.\"",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs that  has \"NoIndex\" Meta tag e.g. ${data[subcategory.data_key][0][0]} . For complete list, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "noindex_page",
            "excel_tab": "noindex_page",
            "order": 5,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:21:02Z",
            "deleted_date": 'null',
            "parentcategory": 3
        },
        {
            "id": 34,
            "title": "Page has nofollow and dofollow incoming internal links",
            "issue_type": 2,
            "description": "A mixture of followed and nofollowed links to a page is most likely a mistake.",
            "risk": "An index-able page could get more \"link juice\" if all internal links to it were followed; followed links to the pages you don't want to be crawled and indexed simply waste the \"link equity.\"",
            "how_to_fix": "Ensure that the reported URLs only get one type of incoming links: either followed or nofollowed.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} pages with both NoFollow and DoFollow incoming internal links e.g. ${data[subcategory.data_key][0][0]} has ${data['count'][subcategory.data_key]} DoFollow and ${data['count'][subcategory.data_key]} NoFollow internal links. For more details refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "page_has_nofollow_dofollow_incoming_internals",
            "excel_tab": "page_has_nofollow_dofollow_inco",
            "order": 10,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:43:48Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 32,
            "title": "Redirected page has no incoming internal links",
            "issue_type": 1,
            "description": "The destination page of the redirect has no incoming internal links.\r\nIn this case also, there is no way your website visitors can access it from your website apart from a redirected URL.",
            "risk": "Search engine crawlers can only discover such pages from the sitemap file or from external backlinks. Website visitors won't be able to get to this page from any other page on your website.",
            "how_to_fix": "Check your website navigation and link architecture to make sure all relevant pages are easily accessible and connected.\r\nConnecting the pages from relevant source may increase visitor flow to these pages.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]}\r\nsuch redirects where the destination page has no incoming internal links ${data[subcategory.data_key][0][0]} has no internal link.\r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "redirected_page_has_no_incoming_internal_links",
            "excel_tab": "redirected_page_has_no_incoming",
            "order": 8,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:40:52Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 30,
            "title": "Page has links to redirect",
            "issue_type": 1,
            "description": "For redirecting URLs on your website, this may not be a big problem, although it is recommend linking to the destination page directly.",
            "risk": "A redirect on an external page you link to requires your attention. Even for internal page redirect, why not directly link to the target page directly avoiding 301?",
            "how_to_fix": "Recommended to replace links to redirecting URLs on the website with direct links.\r\nThis is especially important when linking to external pages. The redirects should be manually reviewed and both the external and internal links to point directly to the target URL.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} URLs with links to pages that redirects to another page. The URL ${data[subcategory.data_key][0][0]} has links to ${data['count'][subcategory.data_key]} internal pages that redirects to another internal page. It is advisable to link to the target URL instead. \r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "page_has_links_to_redirect",
            "excel_tab": "page_has_links_to_redirect",
            "order": 6,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:34:37Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 28,
            "title": "Page has links to broken page",
            "issue_type": 0,
            "description": "Links on website pages that link to internal or external URLs and return one of the 4xx or 5xx HTTP response codes are widely known as \"broken links\".",
            "risk": "Broken links on the website damage  visitors' browsing experience as people cannot access the page or file via a link they click. Besides, broken links create unnecessary \"dead ends\" for the search engine crawlers and can waste the crawl budget.",
            "how_to_fix": "Remove the broken links from the affected pages or replace them with links to other relevant live pages.\r\nAdditionally, you can set redirects for the deleted or moved pages, which is especially relevant for the pages with external backlinks.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} URLs that links to internal or external pages that are broken. The URL ${data[subcategory.data_key][0][0]} links to ${data['count'][subcategory.data_key]} internal URLs and ${data['count'][subcategory.data_key]} external pages which are broken.\r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "page_has_links_to_broken",
            "excel_tab": "page_has_links_to_broken",
            "order": 4,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:33:15Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 27,
            "title": "Orphan page (has no incoming internal links)",
            "issue_type": 0,
            "description": "Orphan pages of a website have no incoming internal links. Ideally a page should have at least one internal link to connect to the site’s user experience.",
            "risk": "Search engine crawlers can only discover such pages from the sitemap file or from external backlinks. Website visitors won't be able to get to this page from any other page on your website.",
            "how_to_fix": "Check your website navigation and link architecture to make sure all relevant pages are easily accessible and connected.\r\nConnecting the pages from relevant source may increase visitor flow to these pages.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} URLs that has no incoming internal links. The URL ${data[subcategory.data_key][0][0]} with 1100 organic visitors has no internal incomig link.\r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "orphan_page_has_no_incoming_internal_links",
            "excel_tab": "orphan_page_has_no_incoming_int",
            "order": 3,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:32:35Z",
            "deleted_date": 'null',
            "parentcategory": 4
        },
        {
            "id": 42,
            "title": "Redirect chain",
            "issue_type": 1,
            "description": "Instead of directly redirect to target URL, at time, redirections are done via another chain of page(s). This is unnecessary and must be avoided.",
            "risk": "Chaining redirects may inflict damage on the user experience, slowing down the page loading speeds. Besides, redirect chains complicate your website's internal linking for the search engine crawlers.",
            "how_to_fix": "For a given URL, replace links to redirecting URLs on these pages with direct links to the final destination URL in the redirect chain.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} redirect chain in the website. The URL ${data[subcategory.data_key][0][0]} redirects to  ${data[subcategory.data_key][0][1]} via ${data[subcategory.data_key][0][2]}\r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "redirect_chain",
            "excel_tab": "redirect_chain",
            "order": 6,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:55:46Z",
            "deleted_date": 'null',
            "parentcategory": 5
        },
        {
            "id": 40,
            "title": "302 Redirect",
            "issue_type": 1,
            "description": "Internal URLs that redirect to another URL with 302 HTTP status code (temporary redirect).\r\n\r\nBoth 302 and 301 redirects pass PageRank as announced by Google.",
            "risk": "However, 302 redirect is a temporary one by definition and should not be used where the redirection is permanent.",
            "how_to_fix": "Review the URLs in this report. If the redirection is permanent, replace the 302 redirects for these URLs with the 301 (Moved Permanently).",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} internal URL redirects that are ${data['count'][subcategory.data_key]} types.The URL ${data[subcategory.data_key][0][0]} is redirected to ${data[subcategory.data_key][0][1]}. But the redirect is 302 i.e. temporary type. If the redirect is permanent, it should be chnaged to 301.\r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "redirect_302",
            "excel_tab": "redirect_302",
            "order": 4,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:54:04Z",
            "deleted_date": 'null',
            "parentcategory": 5
        },
        {
            "id": 39,
            "title": "Redirect loop",
            "issue_type": 0,
            "description": "Redirect loop happens when a URL redirects to itself or when a redirect chain redirects to one of the URLs within the chain. This creates an infinite loop of redirects.",
            "risk": "Redirect loop will typically result in \"Too Many Redirects\" error in the user's browser and will be a \"trap\" for search engine crawlers. That will cause incomplete site crawl.",
            "how_to_fix": "Correct the redirect final destination carefully to avoid loops.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} redirect loop.\r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "redirect_loop",
            "excel_tab": "redirect_loop",
            "order": 3,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:52:44Z",
            "deleted_date": 'null',
            "parentcategory": 5
        },
        {
            "id": 37,
            "title": "Broken redirect",
            "issue_type": 0,
            "description": "Redirects that point to a page returning one of the 4xx or 5xx HTTP response codes.",
            "risk": "These URLs can be accessed neither by your website visitors nor by the search engines crawlers. Crawlers will be forced to abandon the request while people will most likely leave your website.",
            "how_to_fix": "For 4xx HTTP status codes of the destination URLs, replace the links to redirecting URLs on these pages with direct links to relevant live pages or remove these links.\r\nFor 5xx codes, you need to check with your hosting provider or with your web developer. Your server may be overloaded or misconfigured",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]}\r\n internal redirects that points to pages that return 404. The URL ${data[subcategory.data_key][0][0]} is redirected to ${data[subcategory.data_key][0][1]} which returns 404. For complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "broken_redirect",
            "excel_tab": "broken_redirect",
            "order": 1,
            "is_visible": 'true',
            "created_date": "2023-05-02T16:51:04Z",
            "deleted_date": 'null',
            "parentcategory": 5
        },
        {
            "id": 46,
            "title": "Open Graph tags incomplete",
            "issue_type": 1,
            "description": "Pages with one or more of the required Open Graph tags missing.",
            "risk": "The four required Open Graph tags for every page are og:title, og:type, og:image, and og:url.",
            "how_to_fix": "Make sure your pages have all required OG tags if you want them to look good in social feeds when shared.\r\n\r\nPlease note that the URLs inside OG tags must be absolute and utilize the http:// or https:// protocols.\r\n\r\nYou can find more information on the Open Graph protocol",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} URLs that has no incoming internal links. An example URL ${data[subcategory.data_key][0][0]} has no internal incoming link.\r\nFor complete reference of pages, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "og_tags_incomplete",
            "excel_tab": "og_tags_incomplete",
            "order": 2,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:04:57Z",
            "deleted_date": 'null',
            "parentcategory": 6
        },
        {
            "id": 48,
            "title": "Open Graph tags missing",
            "issue_type": 2,
            "description": "",
            "risk": "",
            "how_to_fix": "",
            "more_details": "",
            "data_key": "og_tags_missing",
            "excel_tab": "og_tags_missing",
            "order": 4,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:18:31Z",
            "deleted_date": 'null',
            "parentcategory": 6
        },
        {
            "id": 51,
            "title": "Missing alt text",
            "issue_type": 1,
            "description": "The alt attribute is used to describe your image. Search engines will use it to understand the content of your image files. Also, this text will be shown on your page if the image cannot be displayed.",
            "risk": "Without ALT text, Search engine won't understand the content and context of the image. It's a good practice to provide with ALT text wherever feasible.",
            "how_to_fix": "Make sure each of your images has a concise and descriptive alt text. Corrections are to be done at image level, not by URLs.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]}\r\n URLs that has images without ALT text mentioned. The URL ${data[subcategory.data_key][0][0]} has 36 images without ALT text. For complete list, refer to tab sheet \"${subcategory.excel_tab}\". Even though the number of image count appears too high, there are repetitions and hence the numbers are not that high as it sounds.",
            "data_key": "image_alt_missing",
            "excel_tab": "image_alt_missing",
            "order": 2,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:24:55Z",
            "deleted_date": 'null',
            "parentcategory": 7
        },
        {
            "id": 50,
            "title": "HTTPS&nbsp;&nbsp; page links to HTTP&nbsp;&nbsp; image",
            "issue_type": 1,
            "description": "This issue is an instance of mixed content that occurs when HTML pages load over a secure HTTPS connection but link to resources (images, CSS, or JS) over an insecure HTTP connection.",
            "risk": "Mixed content degrades the security and user experience of your HTTPS site.\r\n\r\nSome browsers block insecure resource requests by default. If the web page depends on these insecure resources, then the page might not work properly when they get blocked.",
            "how_to_fix": "Serve all content as HTTPS and fix the links. Often, the HTTPS version of the content already exists and this just requires adding an \"s\" to links - http:// to https://.\r\n\r\nFor images hosted on other domains, use the site's HTTPS version if available. If HTTPS is not available, you can try contacting the domain and asking them if they can make the content available via HTTPS.",
            "more_details": "Ahref bot detected ${data['count'][subcategory.data_key]} URLs that has reference to resources from insecure sources. The URL ${data[subcategory.data_key][0][0]}\r\nrefers to insecure resources.",
            "data_key": "HTTPS_page_links_to_HTTP_image",
            "excel_tab": "HTTPS_page_links_to_HTTP_image",
            "order": 1,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:24:05Z",
            "deleted_date": 'null',
            "parentcategory": 7
        },
        {
            "id": 57,
            "title": "Noindex page in sitemap",
            "issue_type": 0,
            "description": "There are pages in the sitemap.xml that are marked \"NoIndex\". Either the pages be indexable or they should be removed from sitemap.",
            "risk": "This will lead unnecessary crawling by Google bot. This is conflicting, needs review and correction.",
            "how_to_fix": "This will lead unnecessary crawling by Google bot. This is conflicting, needs review and correction.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]}\r\n URLs that that has \"NoIndex\" Meta tag and are included in the sitemap. For complete list, refer to tab sheet \"${subcategory.excel_tab}\".",
            "data_key": "noindex_page_in_sitemap",
            "excel_tab": "noindex_page_in_sitemap",
            "order": 6,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:30:44Z",
            "deleted_date": 'null',
            "parentcategory": 8
        },
        {
            "id": 56,
            "title": "Double slash in URL",
            "issue_type": 0,
            "description": "There are URLs that contain a double slash (after the domain part).",
            "risk": "Most servers are set up to ignore a double slash in the URL path. However, such URLs may be confusing for search engines as they will be interpreted as stand-alone URLs, which can result in duplicate content issues.",
            "how_to_fix": "Review the URLs in this report and remove the unnecessary double slashes from their permalinks.\r\nAfter that, you can check the internal backlinks to the URLs with a double slash and point them to the corrected URL. This will prevent some unnecessary redirects on your website.",
            "more_details": "Google bot detected ${data['count'][subcategory.data_key]} URLs that that has longer than desired title tag. An example URL is ${data[subcategory.data_key][0][0]} For complete list, refer to tab sheet \"${subcategory.excel_tab}\"",
            "data_key": "double_slash_in_url",
            "excel_tab": "double_slash_in_url",
            "order": 5,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:30:16Z",
            "deleted_date": 'null',
            "parentcategory": 8
        },
        {
            "id": 52,
            "title": "3XX redirect in sitemap",
            "issue_type": 0,
            "description": "URLs included in sitemap file that redirect.\r\n\r\nSitemap must list all the pages desired by search engines to crawl and index.",
            "risk": "Redirecting URLs in sitemaps can result in indexability issues on your website.",
            "how_to_fix": "Replace the redirecting URLs in the sitemaps with the destination URL. If the destination URL is already listed, simply remove the URL that redirects to it from the sitemap file",
            "more_details": "Ahref bot detected  ${data['count'][subcategory.data_key]} URLs in the sitemap that are further redirected to another URL. \r\n${data[subcategory.data_key][0][0]} is redirected to ${data[subcategory.data_key][0][1]} ${data[subcategory.data_key][0][2]} is already in the sitemap. So, just remove this entry from sitemap. For more details, refer to tab \"${subcategory.excel_tab}\"",
            "data_key": "redirect_3XX_in_sitemap",
            "excel_tab": "redirect_3XX_in_sitemap",
            "order": 1,
            "is_visible": 'true',
            "created_date": "2023-05-02T17:27:47Z",
            "deleted_date": 'null',
            "parentcategory": 8
        }
    ]
    }
    # print("1")
    itemCount = 0
    for key in data['count']:
        if data['count'][key] > 0:
            itemCount += 1
    
    progress = 86
    
    def getColorFromGradient(progress):
        if 0 <= progress <= 49:
            start_color = [255, 0, 0]  # Red
            end_color = [255, 205, 0]  # Orange
            percent = progress / 49
        else:
            start_color = [255, 205, 0]  # Orange
            end_color = [0, 128, 0]  # Green
            percent = (progress - 49) / 51

        r = int(start_color[0] + (end_color[0] - start_color[0]) * percent)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * percent)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * percent)

        hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
        return hex_color

    def getLabelColorAndBackgroundColor(progress):
        label = None
        color = None

        if 0 <= progress <= 29:
            label = "Weak"
            color = "#F6B300"
        elif 30 <= progress <= 70:
            label = "Fair"
            color = "#99B925"
        elif 71 <= progress <= 89:
            label = "Good"
            color = "#36A64B"
        elif 90 <= progress <= 100:
            label = "Excellent"
            color = "#009C5D"

        red = 255 - (progress * 255) / 100
        green = (progress * 128) / 100

        return {'label': label, 'color': color}

    res = getLabelColorAndBackgroundColor(progress)
    label = res['label']
    color = res['color']
    bg_hex_color = getColorFromGradient(progress)

    pdf_file_name = 'audit_report1.pdf'
    # Get the template and context data
    template = get_template('test.html')
    # print("2")
    context = {'title': 'My PDF', 'domain': 'tistasoft.com', 'reporting_time': reporting_time, 'data': data, 'timeMarkerInSecond': 8, 'list': list, 'issues': issues, 'itemCount': itemCount, 'progress': progress, 'label': label, 'color': color, 'bg_hex_color': bg_hex_color}
    # print("2")
    # Render the template with context data
    html = template.render(context)

    # Generate the PDF using WeasyPrint
    # pdf_file = HTML(string=html).write_pdf()
    pdf_file = HTML(string=html, base_url=settings.STATIC_URL).write_pdf()
    # pdf_file = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[settings.STATIC_ROOT + 'test.css'])

    # Save the PDF to a file path
    # file_path = f'{pdf_file_name}'
    project_dir = os.getcwd()
    file_path = os.path.join(project_dir, pdf_file_name)
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

# from client import RestClient
# from rest_client import RestClient
def business_listing(request):
    # You can download this file from here https://cdn.dataforseo.com/v3/examples/python/python_Client.zip
    # client = RestClient("anarul.haque@tistasoft.com", "efff2862e4f6d350")
    client = ''
    post_data = dict()
    # simple way to set a task
    post_data[len(post_data)] = dict(
        categories=[
            "pizza_restaurant"
        ],
        description="pizza",
        title="pizza",
        is_claimed=True,
        location_coordinate="53.476225,-2.243572,10",
        initial_dataset_filters=[
            ["rating.value",">",3]
        ],
        internal_list_limit=10,
        limit=3
    )
    # POST /v3/business_data/business_listings/categories_aggregation/live
    response = client.post("/v3/business_data/business_listings/categories_aggregation/live", post_data)
    # you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
    if response["status_code"] == 20000:
        print(response)
        # do something with result
    else:
        print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
