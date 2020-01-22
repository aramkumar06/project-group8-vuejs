package com.ssafy.model.dao;

import java.util.List;
import org.apache.ibatis.annotations.Mapper;
import com.ssafy.model.dto.Youtuber;

@Mapper
public interface YoutuberDao {
	public List<Youtuber> search(String name);
	public List<Youtuber> searchAll();
	public void insert(Youtuber youtuber);
}
