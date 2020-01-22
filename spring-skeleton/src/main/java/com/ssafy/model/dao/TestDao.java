package com.ssafy.model.dao;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.Test;

@Mapper
public interface TestDao {
	public List<Test> search_all();
	public void insert(Test test);
}
