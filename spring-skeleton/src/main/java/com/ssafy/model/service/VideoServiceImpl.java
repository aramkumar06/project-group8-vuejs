package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.VideoDao;
import com.ssafy.model.dto.Video;

@Service
public class VideoServiceImpl implements VideoService {

	@Autowired
	private VideoDao dao;
	
	@Override
	public Video search(int vno) {
		try {
			return dao.search(vno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("video 고유번호 조회 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<Video> searchKeyword(String keyword) {
		try {
			return dao.searchKeyword(keyword);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("video 정보 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public List<Video> searchAll() {
		try {
			return dao.searchAll();
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("video 전체 목록 조회 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<Video> searchRanking(Map<String, String> condition) {
		try {
			return dao.searchRanking(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("video 랭킹 조회 중 에러가 발생했습니다.");
		}
	}
}