package com.ssafy.model.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.TestDao;
import com.ssafy.model.dto.Test;


@Service
public class TestServiceImpl implements TestService {

	@Autowired
	private TestDao dao;
	
	@Override
	public List<Test> search_all() {
		try {
			return dao.search_all();
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("test 조회 중 에러 발생");
		}
	}

	@Override
	public void insert(Test test) {
		try {
			dao.insert(test);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("test 등록 중 에러 발생");
		}
	}

}
