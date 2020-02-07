package com.ssafy.model.dao;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.ssafy.model.dto.User;
import com.ssafy.model.dto.Youtuber;

@Mapper
public interface UserDao {
	public void insertUser(User user);
	public User search(String userID);
	public List<Youtuber> searchUserFavoriteYoutuber(String userID);
	public int searchUserExist(String userID);
}