package com.ssafy.model.dto;

public class Test {
	int id;
	String value;
	
	public Test(){}

	public Test(int id, String value) {
		super();
		this.id = id;
		this.value = value;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getValue() {
		return value;
	}

	public void setValue(String value) {
		this.value = value;
	}

	@Override
	public String toString() {
		return "Test [id=" + id + ", value=" + value + "]";
	}
	
	
}
