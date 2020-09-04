//
//  AddCourseViewController.m
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "AddCourseViewController.h"

@interface AddCourseViewController ()

@end

@implementation AddCourseViewController

@synthesize txtName;
@synthesize delegate;
@synthesize inputCourse;

- (void)viewDidLoad {
    [super viewDidLoad];
    
    if (inputCourse) {
        [txtName setText:inputCourse.courseName];
    } else {
        [txtName setPlaceholder:@"Input course name"];
    }
}

#pragma mark - Actions

- (IBAction)closeView:(id)sender {
    [self dismissViewControllerAnimated:true completion:nil];
}

- (IBAction)saveCourse:(id)sender {
    if (txtName.text.length >= 3) {
        BOOL success;
        
        if (inputCourse) {
            inputCourse.courseName = txtName.text;
            success = [[ContentManager sharedManager] editCourse:inputCourse];
        } else {
            success = [[ContentManager sharedManager] insertCourseWithName:txtName.text];
        }
        
        if(delegate != nil && [delegate respondsToSelector:@selector(addCourseViewControllerSaveWithFlag:)]) {
            [delegate addCourseViewControllerSaveWithFlag:success];
        }
        
        [self dismissViewControllerAnimated:YES completion:nil];
    } else {
        NSLog(@"you must input name lenght >= 3");
    }
}

@end
