package com.ssafy.model.dao;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.News;

@Mapper
public interface NewsDao {
	public News search(int nno);
	public List<News> searchKeyword(String keyword);
	public List<News> searchAll();
	public List<News> searchRanking(Map<String, String> condition);
}
