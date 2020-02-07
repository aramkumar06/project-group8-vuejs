package com.ssafy.model.dto;

public class Category {
	//category 테이블 + category_youtuber_relation 테이블의 컬럼을 합쳐놓은 DTO
	private int cano;
	private String name;
	private int clickCount;
	private String imageLink;
	
	private int cyno;			//category_youtuber_relation 테이블의 컬럼
	private int yno;			//category_youtuber_relation 테이블의 컬럼
	
	public int getCano() {
		return cano;
	}
	
	public void setCano(int cano) {
		this.cano = cano;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getClickCount() {
		return clickCount;
	}
	public void setClickCount(int clickCount) {
		this.clickCount = clickCount;
	}
	public String getImageLink() {
		return imageLink;
	}
	public void setImageLink(String imageLink) {
		this.imageLink = imageLink;
	}
	public int getCyno() {
		return cyno;
	}
	public void setCyno(int cyno) {
		this.cyno = cyno;
	}
	public int getYno() {
		return yno;
	}
	public void setYno(int yno) {
		this.yno = yno;
	}
}