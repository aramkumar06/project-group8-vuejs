package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import com.ssafy.model.dto.Trend;
import com.ssafy.model.dto.Category;
import com.ssafy.model.dto.News;
import com.ssafy.model.dto.Video;
import com.ssafy.model.dto.Youtuber;

public interface YoutuberService {
	public Youtuber search(int yno);
	public List<Category> searchCategoryList(int yno);
	public List<Youtuber> searchKeyword(String keyword);
	public List<Youtuber> searchAll();
	public List<Youtuber> searchRanking(Map<String, String> condition);
	public List<News> searchNews(int yno);
	public List<Video> searchVideo(int yno);
//	public List<Video> searchCommunity(int yno);
	public List<Trend> searchTrend(int yno);
	public List<Video> searchVideoGoodRatio(Map<String, Integer> condition);
	public double searchGoodRatio(Map<String, Integer> condition);
	public int searchVideoCount(Map<String, Integer> condition);
	public List<Integer> searchTermVideoCount(Map<String, Integer> condition);
}