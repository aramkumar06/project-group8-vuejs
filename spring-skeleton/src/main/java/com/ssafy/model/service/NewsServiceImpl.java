package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.NewsDao;
import com.ssafy.model.dto.News;

@Service
public class NewsServiceImpl implements NewsService {

	@Autowired
	private NewsDao dao;
	
	@Override
	public News search(int nno) {
		try {
			return dao.search(nno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("news 고유번호 조회 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<News> searchKeyword(String keyword) {
		try {
			return dao.searchKeyword(keyword);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("News 정보 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public List<News> searchAll() {
		try {
			return dao.searchAll();
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("news 전체 목록 조회 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<News> searchRanking(Map<String, String> condition) {
		try {
			return dao.searchRanking(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("news 랭킹 조회 중 에러가 발생했습니다.");
		}
	}
}