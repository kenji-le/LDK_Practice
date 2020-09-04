//
//  AddStudentViewController.h
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol AddStudentViewControllerDelegate <NSObject>

@optional
-(void)addStudentViewControllerSaveWithFlag:(BOOL)flag;

@end

@interface AddStudentViewController : UIViewController

@property (nonatomic, weak) IBOutlet UITextField *txtName;
@property (nonatomic, weak) id<AddStudentViewControllerDelegate> delegate;
@property (nonatomic, strong) Student *inputStudent;
@property (nonatomic, strong) Course *inputCourse;

@end
