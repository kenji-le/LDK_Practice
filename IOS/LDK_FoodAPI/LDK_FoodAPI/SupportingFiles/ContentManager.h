//
//  ContentManager.h
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "AFNetworking.h"

@interface ContentManager : NSObject
{
    AFHTTPSessionManager *manager;
}

+ (ContentManager *)sharedManager;

- (void)getFoodListWithCompletion:(void (^)(BOOL, NSArray *, NSString *))callback;

@end
