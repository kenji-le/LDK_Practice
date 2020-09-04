//
//  AddStudentViewController.m
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "AddStudentViewController.h"

@interface AddStudentViewController ()

@end

@implementation AddStudentViewController

@synthesize txtName;
@synthesize delegate;
@synthesize inputStudent;
@synthesize inputCourse;

- (void)viewDidLoad {
    [super viewDidLoad];
    
    if (inputStudent) {
        [txtName setText:inputStudent.studentName];
    } else {
        [txtName setPlaceholder:@"Input student name"];
    }
}

#pragma mark - Actions

- (IBAction)closeView:(id)sender {
    [self dismissViewControllerAnimated:true completion:nil];
}

- (IBAction)saveStudent:(id)sender {
    if (txtName.text.length >=3 ) {
        BOOL success;
        
        if (inputStudent) {
            inputStudent.studentName = txtName.text;
            success = [[ContentManager sharedManager] editStudent:inputStudent];
        } else {
            success = [[ContentManager sharedManager] addStudentName:txtName.text inCourse:inputCourse];
        }
        
        if (delegate != nil && [delegate respondsToSelector:@selector(addStudentViewControllerSaveWithFlag:)]) {
            [delegate addStudentViewControllerSaveWithFlag:success];
        }
        
        [self dismissViewControllerAnimated:YES completion:nil];
    } else {
        NSLog(@"you must input name lenght >= 3");
    }
}

@end

