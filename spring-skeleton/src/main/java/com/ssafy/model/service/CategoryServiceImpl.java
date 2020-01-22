package com.ssafy.model.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.CategoryDao;
import com.ssafy.model.dto.Category;
import com.ssafy.model.dto.Youtuber;

@Service
public class CategoryServiceImpl implements CategoryService {

	@Autowired
	private CategoryDao dao;
	
	@Override
	public List<Youtuber> search(int cano) {
		try {
			return dao.search(cano);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 고유번호 조회 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<Category> searchAll() {
		try {
			return dao.searchAll();
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 전체 목록 조회 중 에러가 발생했습니다.");
		}
	}
}