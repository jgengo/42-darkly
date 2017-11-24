#!/usr/bin/env ruby

require 'rubygems'
require 'nokogiri'
require 'open-uri'

class Crawler
	attr_accessor :url
	attr_accessor :path
	attr_accessor :nok

	def initialize(url, path = '/')
		@url = url
		@path = path
		@nok = Nokogiri::HTML(open(url + path))
		self.get_links_in(@nok)
	end

	def get_links_in(nok)
		links = nok.css('a')

		links.each do |l|
			subpath = l['href']
			if subpath.split('').last != '/'
				open_file = open(@url + @path + subpath).read
				# puts "#{@path + subpath}"
				puts "#{open_file}"
			end
			sleep(0.1)
			Crawler.new(@url, @path + subpath) if (subpath != '../' and subpath != 'README')
		end

	end
end

if ARGV.count == 1
	Crawler.new(ARGV[0])
elsif ARGV.count == 2
	Crawler.new(ARGV[0], ARGV[1])
else 
	p "usage: ./script.rb <url> [<path>]"
	p "exemple: ./script.rb http://192.168.1.1/ .hidden/"
end
