package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import com.ssafy.model.dto.Video;

public interface VideoService {
	public Video search(int vno);
	public List<Video> searchKeyword(String keyword);
	public List<Video> searchAll();
	public List<Video> searchRanking(Map<String, String> condition);
}