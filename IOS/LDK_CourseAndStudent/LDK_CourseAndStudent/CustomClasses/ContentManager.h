//
//  ContentManager.h
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface ContentManager : NSObject

+ (ContentManager *)sharedManager;

- (NSArray *)getAllCourses;
- (BOOL)insertCourseWithName:(NSString *)name;
- (BOOL)editCourse:(Course *)course;
- (BOOL)deleteCourse:(Course *)course;

//- (NSArray *)getAllStudents;
- (BOOL)addStudentName:(NSString *)name inCourse:(Course *)course;
- (BOOL)editStudent:(Student *)student;
- (BOOL)deleteStudent:(Student *)student;
//- (NSArray *)getStudentsWithCourse:(NSString *)course;

@end
