package com.ssafy.model.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.YoutuberDao;
import com.ssafy.model.dto.Youtuber;

@Service
public class YoutuberServiceImpl implements YoutuberService {

	@Autowired
	private YoutuberDao dao;
	
	@Override
	public List<Youtuber> search(String name) {
		try {
			return dao.search(name);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 이름 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public List<Youtuber> searchAll() {
		try {
			return dao.searchAll();
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 목록 조회 중 에러가 발생했습니다.");
		}
	}

	@Override
	public void insert(Youtuber youtuber) {
		try {
			dao.insert(youtuber);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("youtuber 등록 중 에러 발생");
		}
	}
}
