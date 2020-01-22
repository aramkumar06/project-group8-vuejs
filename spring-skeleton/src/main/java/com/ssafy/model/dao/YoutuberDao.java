package com.ssafy.model.dao;

import java.util.List;
import java.util.Map;
import org.apache.ibatis.annotations.Mapper;
import com.ssafy.model.dto.Youtuber;

@Mapper
public interface YoutuberDao {
	public Youtuber search(int yno);
	public List<Youtuber> searchKeyword(String keyword);
	public List<Youtuber> searchAll();
	public List<Youtuber> searchRanking(Map<String, String> condition);
	public void insert(Youtuber youtuber);
}
