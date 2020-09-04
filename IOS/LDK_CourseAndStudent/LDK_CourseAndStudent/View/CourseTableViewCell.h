//
//  CourseTableViewCell.h
//  LDK_CourseAndStudent
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol CourseTableViewCellDelegate <NSObject>

@optional
- (void)courseTableViewCellDeleteAtIndex:(NSIndexPath *)index;
- (void)courseTableViewCellEditAtIndex:(NSIndexPath *)index;

@end

@interface CourseTableViewCell : UITableViewCell
{
    NSIndexPath *currentIndex;
}

@property (nonatomic,weak) IBOutlet UILabel *lblName;
@property (nonatomic,weak) id<CourseTableViewCellDelegate> delegate;

- (void)setCellWithCourse:(Course *)course atIndex:(NSIndexPath *)index;

@end
