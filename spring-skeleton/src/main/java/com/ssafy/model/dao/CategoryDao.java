package com.ssafy.model.dao;

import java.util.List;
import java.util.Map;
import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.Category;
import com.ssafy.model.dto.Youtuber;

@Mapper
public interface CategoryDao {
	public List<Youtuber> search(int cano);
	public List<Category> searchAll();
}
