//
//  ContentManager.m
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "ContentManager.h"

@implementation ContentManager

+ (ContentManager *)sharedManager {
    static ContentManager *manager = nil;
    static dispatch_once_t onceToken;
    
    dispatch_once(&onceToken, ^{
        manager = [[ContentManager alloc]init];
    });
    
    return manager;
}

- (NSManagedObjectContext *)getCurrentContext {
    AppDelegate *application = (AppDelegate *)[[UIApplication sharedApplication] delegate];
    return application.persistentContainer.viewContext;
}

# pragma mark - Course handling

- (NSArray *)getAllCourses {
    // Get current context of app
    NSManagedObjectContext *context = [self getCurrentContext];
    
    // Create fetch request
    NSFetchRequest *request = [Course fetchRequest];
    
    // set sort column. If you want to multi sort, crate multi sort descriptor
    NSSortDescriptor *sort = [NSSortDescriptor sortDescriptorWithKey:@"courseName" ascending:YES];
    request.sortDescriptors = @[sort];
    
    NSError *error = nil;
    return [context executeFetchRequest:request error:&error];
}

- (BOOL)insertCourseWithName:(NSString *)name {
    // Get current context of app
    NSManagedObjectContext *context = [self getCurrentContext];
    
    // Make insert request
    Course *course = [NSEntityDescription insertNewObjectForEntityForName:@"Course" inManagedObjectContext:context];
    course.courseName = name;
    
    NSError *error = nil;
    if (![context save:&error]) {
        return NO;
    } else {
        return YES;
    }
}

- (BOOL)editCourse:(Course *)course {
    if (course) {
        NSManagedObjectContext *context = [self getCurrentContext];
        NSError *error = nil;
        if ([context save:&error]) {
            return YES;
        }
    }
    
    return NO;
}

- (BOOL)deleteCourse:(Course *)course {
    // get current context of app
    NSManagedObjectContext *context = [self getCurrentContext];
    [context deleteObject:course];
    NSError *error = nil;
    if ([context save:&error]) {
        return YES;
    } else {
        return NO;
    }
}

#pragma mark - Student handling

- (NSArray *)getStudentsWithCourse:(NSString *)course {
    // Get current context of app
    NSManagedObjectContext *context = [self getCurrentContext];
    
    // Create fetch request
    NSFetchRequest *request = [Student fetchRequest];
    
    // set sort column. If you want to multi sort, crate multi sort descriptor
    NSSortDescriptor *sort = [NSSortDescriptor sortDescriptorWithKey:@"studentName" ascending:YES];
    request.sortDescriptors = @[sort];
    
    // set search predicate
    NSPredicate *predicate = [NSPredicate predicateWithFormat:@"inCourse.courseName ==[c] %@", course];
    [request setPredicate:predicate];
    
    NSError *error = nil;
    return [context executeFetchRequest:request error:&error];
}

- (BOOL)addStudentName:(NSString *)name inCourse:(Course *)course {
    // Get current context of app
    NSManagedObjectContext *context = [self getCurrentContext];
    
    // Make insert request
    Student *student = [NSEntityDescription insertNewObjectForEntityForName:@"Student" inManagedObjectContext:context];
    student.studentName = name;
    student.inCourse = course;
    
    NSError *error = nil;
    if (![context save:&error]) {
        return NO;
    } else {
        return YES;
    }
}

- (BOOL)editStudent:(Student *)student {
    if (student) {
        NSManagedObjectContext *context = [self getCurrentContext];
        NSError *error = nil;
        if ([context save:&error]) {
            return YES;
        }
    }
    
    return NO;
}

- (BOOL)deleteStudent:(Student *)student {
    // get current context of app
    NSManagedObjectContext *context = [self getCurrentContext];
    [context deleteObject:student];
    
    NSError *error = nil;
    if ([context save:&error]) {
        return YES;
    } else {
        return NO;
    }
}

@end
