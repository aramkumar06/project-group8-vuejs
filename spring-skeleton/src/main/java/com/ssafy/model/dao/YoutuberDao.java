package com.ssafy.model.dao;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.Category;
import com.ssafy.model.dto.News;
import com.ssafy.model.dto.Trend;
import com.ssafy.model.dto.Video;
import com.ssafy.model.dto.Youtuber;

@Mapper
public interface YoutuberDao {
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
