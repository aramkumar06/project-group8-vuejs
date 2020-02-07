package com.ssafy.model.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.FavoriteDao;
import com.ssafy.model.dto.Favorite;
import com.ssafy.model.dto.Youtuber;

@Service
public class FavoriteServiceImpl implements FavoriteService {
	
	@Autowired
	private FavoriteDao dao;
	
	@Override
	public void insertFavorite(Favorite favorite) {
		try {
			dao.insertFavorite(favorite);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("즐겨찾기 추가 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public void deleteFavorite(Map<String, Integer> condition) {
		try {
			dao.deleteFavorite(condition);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("즐겨찾기 삭제 중 에러가 발생했습니다.");
		}
	}

	@Override
	public List<Youtuber> searchUserFavoriteYoutuber(int usno) {
		try {
			return dao.searchUserFavoriteYoutuber(usno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("사용자가 즐겨찾기 한 유투버 목록 조회 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public int searchYoutuberFavoriteNum(int yno) {
		try {
			return dao.searchYoutuberFavoriteNum(yno);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("유투버 고유번호로 해당 유투버를 즐겨찾기 한 사람 수 조회 중 에러가 발생했습니다.");
		}
	}
}