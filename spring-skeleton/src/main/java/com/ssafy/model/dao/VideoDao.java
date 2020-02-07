package com.ssafy.model.dao;

import java.util.List;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.Video;

@Mapper
public interface VideoDao {
	public Video search(int vno);
	public List<Video> searchKeyword(String keyword);
	public List<Video> searchAll();
	public List<Video> searchRanking(Map<String, String> condition);
}
