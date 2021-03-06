# -*- coding: utf-8 -*-

from django.template.base import Node, NodeList, Template, Context, Variable
from django import template
from django.template import TemplateSyntaxError

from www.settings import NEWS_IN_MAIN as nm

from article.models import Article

register = template.Library()

################################################################################################################
################################################################################################################

class GetNewsListNode(Node):
	def render(self, context):
		context['news_list'] = Article.activs.all()[:nm]
		return ''
		
def get_news_list(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 1: raise TemplateSyntaxError("%r take > 1 argument" % bits[0])
	return GetNewsListNode()
	
get_news_list = register.tag(get_news_list)

################################################################################################################
################################################################################################################