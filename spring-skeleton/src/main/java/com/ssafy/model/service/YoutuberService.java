package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import com.ssafy.model.dto.Youtuber;

public interface YoutuberService {
	public Youtuber search(int yno);
	public List<Youtuber> searchKeyword(String keyword);
	public List<Youtuber> searchAll();
	public List<Youtuber> searchRanking(Map<String, String> condition);
	public void insert(Youtuber youtuber);
}