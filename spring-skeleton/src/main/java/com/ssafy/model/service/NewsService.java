package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import com.ssafy.model.dto.News;

public interface NewsService {
	public News search(int nno);
	public List<News> searchKeyword(String keyword);
	public List<News> searchAll();
	public List<News> searchRanking(Map<String, String> condition);
}