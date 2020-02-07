package com.ssafy.model.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.model.dao.UserDao;
import com.ssafy.model.dto.User;
import com.ssafy.model.dto.Youtuber;


@Service
public class UserServiceImpl implements UserService {
	
	@Autowired
	private UserDao dao;

	@Override
	public void insertUser(User user) {
		try {
			dao.insertUser(user);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("사용자 추가 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public User search(String userID) {
		try {
			return dao.search(userID);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("사용자 정보 검색 중 에러가 발생했습니다.");
		}
	}
	
	@Override
	public List<Youtuber> searchUserFavoriteYoutuber(String userID) {
		try {
			return dao.searchUserFavoriteYoutuber(userID);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("userID로 즐겨찾기 정보 검색 중 에러가 발생했습니다.");
		}
	}

	@Override
	public int searchUserExist(String userID) {
		try {
			return dao.searchUserExist(userID);
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException("userID로 회원 가입 여부 조회 중 에러가 발생했습니다.");
		}
	}
}