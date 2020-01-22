package com.ssafy.model.service;

import java.util.List;

import com.ssafy.model.dto.Test;

public interface TestService {
	public List<Test> search_all();
	public void insert(Test test);
}
